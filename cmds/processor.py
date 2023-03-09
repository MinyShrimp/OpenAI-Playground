import re
import traceback
from enum import Enum

from common import log
from common import MultiKeyDict

'''
Since: 2023-03-08
Author: 김회민 ksk7584@gmail.com
'''


class CommandProcessor(object):
    """ 명령어 처리 클래스

    Singleton 패턴 적용: CommandProcessor()
    """
    __INSTANCE = None

    # 커멘드 초기 설정 템플릿
    __COMMANDS = {
        "h": {
            "description": "show all commands",
            "supports": ["help"],
        },
        "q": {
            "description": "program exit",
            "supports": ["quit"],
        }
    }

    # 커멘드를 실제로 관리하기 위한 멀티 키 딕셔너리
    __COMMANDS_MULTI = MultiKeyDict()

    # help 커멘드 출력을 위한 리스트
    __COMMANDS_DECS = []

    @staticmethod
    class ReturnStatus(Enum):
        """ 프로세스 로직 흐름 처리를 위한 Enum

        * OK:      정상 처리
        * QUIT:    프로그램 종료
        * UNKNOWN: 등록되지 않은 커멘드
        """
        OK = 1
        QUIT = -1
        UNKNOWN = 0

    def __init__(self):
        """ 초기 설정
        """
        cls = type(self)
        if not hasattr(cls, "_init"):
            cls._init = True

            self.__COMMANDS["h"]["do"] = self.__help_do
            self.__COMMANDS["q"]["do"] = self.__quit_do

            self.__COMMANDS_MULTI.bulk_add(self.__COMMANDS)
            self.__COMMANDS_DECS = [
                self.__get_help_str(keys, value["description"]) for keys, value in self.__COMMANDS_MULTI.items()
            ]

            log.debug("Finished Initalizing %s", cls.__INSTANCE)

    def __new__(cls):
        """ 싱글톤 패턴 처리
        """
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(CommandProcessor, cls).__new__(cls)
            log.debug("Created new instance %s", cls.__INSTANCE)
        return cls.__INSTANCE

    @staticmethod
    def __get_help_str(keys: list[str], desc: str):
        return "- '{}': {}".format("', '".join(keys), desc)

    def __add_decs(self, cmds: list[tuple[list[str], dict]]):
        self.__COMMANDS_DECS.append(
            *[self.__get_help_str(keys, value["description"]) for keys, value in cmds]
        )

    def __help_do(self, *args, **params) -> ReturnStatus:
        """ "help" Command 처리

        :return: CommandProcessor.ReturnStatus.OK
        """
        print("commands list")
        for desc in self.__COMMANDS_DECS:
            print(desc)
        return CommandProcessor.ReturnStatus.OK

    @staticmethod
    def __quit_do(*args, **params) -> ReturnStatus:
        """ "quit" Command 처리

        :return: CommandProcessor.ReturnStatus.QUIT
        """
        return CommandProcessor.ReturnStatus.QUIT

    def bulk_add_commands(self, _dict: dict):
        results = self.__COMMANDS_MULTI.bulk_add(_dict)
        self.__add_decs(results)
        return results

    def add_command(self, key: str, value: dict):
        """ 커멘드 1 개 추가
        :param key: commands main key
        :param value: { "description": str, "supports": list[str], "do": Callable[[], None] }
        :return: 추가된 커멘드 반환
        """
        result = self.__COMMANDS_MULTI.add(key, value)
        self.__add_decs([result])
        return result

    @staticmethod
    def __cmd_params(command: str) -> tuple[str, dict]:
        """ `-` 를 기준으로 함수와 파라미터를 분리

        * `$ help -i a, b, c`
        * => `_command = "help", _params = { 'i': ["a", "b", "c"] }`

        :param command:
        :return: (_command: str, _params: dict)
        """
        _command_compile = re.compile("^[a-z ]+")
        _params_complie_1 = re.compile('(-[a-z_]+ +("[^"]+" ?)+)')
        _params_complie_2 = re.compile('"([^"]+)"')

        _command, _params = command, None
        if '-' in command:
            _command = _command_compile.match(command).group()
            _tmps = [_tmp[0].strip()[1:] for _tmp in _params_complie_1.findall(command)]

            _params = {}
            for _t in _tmps:
                _head = _t.split(" ")[0]
                _values = _params_complie_2.findall(_t)
                _params[_head] = _values

        _command = _command.strip()
        log.debug("cmd: %s, params: %s", _command, _params)
        return _command, _params

    def __process(self, command: str) -> ReturnStatus:
        """ 실제 커멘트 처리

        :param command:
        :return: CommandProcessor.ReturnStatus.UNKNOWN
        """
        command = command.replace("\n", "").strip()
        if command == "":
            return CommandProcessor.ReturnStatus.OK

        _command, _params = self.__cmd_params(command)

        value = self.__COMMANDS_MULTI.get(_command)
        if value is None:
            return CommandProcessor.ReturnStatus.UNKNOWN

        if _params is None:
            return value["do"]()
        else:
            return value["do"](**_params)

    def process(self):
        log.info("Hello, Welcome to My Program !!!")
        result = CommandProcessor.ReturnStatus.OK
        while result is not CommandProcessor.ReturnStatus.QUIT:
            try:
                print("=======================================")
                input_data = input("Input Command (To help, type 'h' or 'help'): ")
                print()

                result = self.__process(input_data)
                if result is CommandProcessor.ReturnStatus.UNKNOWN:
                    print("Unvalid Command: '{}'".format(input_data))
                    print("Type 'h' or 'help' to show all commands")
            except Exception:
                log.warning(traceback.format_exc())

        log.info("Program exit")
