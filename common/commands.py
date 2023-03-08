from enum import Enum

from . import MultiKeyDict
from . import Logger

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
        self.__COMMANDS["h"]["do"] = self.__help_do
        self.__COMMANDS["q"]["do"] = self.__quit_do

        self.__COMMANDS_MULTI.bulk_add(self.__COMMANDS)
        self.__COMMANDS_DECS = [
            self.__get_help_str(keys, value["description"]) for keys, value in self.__COMMANDS_MULTI.items()
        ]

    def __new__(cls):
        """ 싱글톤 패턴 처리
        """
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(CommandProcessor, cls).__new__(cls)
        return cls.__INSTANCE

    @staticmethod
    def __get_help_str(keys: list[str], desc: str):
        return "- '{}': {}".format("' or '".join(keys), desc)

    def __add_decs(self, cmds: list[tuple[list[str], dict]]):
        self.__COMMANDS_DECS.append(
            *[self.__get_help_str(keys, value["description"]) for keys, value in cmds]
        )

    def __help_do(self) -> ReturnStatus:
        """ "help" Command 처리

        :return: CommandProcessor.ReturnStatus.OK
        """
        print("commands list")
        for desc in self.__COMMANDS_DECS:
            print(desc)
        return CommandProcessor.ReturnStatus.OK

    @staticmethod
    def __quit_do() -> ReturnStatus:
        """ "quit" Command 처리

        :return: CommandProcessor.ReturnStatus.QUIT
        """
        print("Good bye")
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

    def __process(self, command: str) -> ReturnStatus:
        """ 실제 커멘트 처리

        :param command:
        :return: CommandProcessor.ReturnStatus.UNKNOWN
        """
        command = command.replace("\n", "").strip()
        if command == "":
            return CommandProcessor.ReturnStatus.OK
        value = self.__COMMANDS_MULTI.get(command)
        if value is None:
            return CommandProcessor.ReturnStatus.UNKNOWN

        return value["do"]()

    def process(self):
        result = CommandProcessor.ReturnStatus.OK
        while result is not CommandProcessor.ReturnStatus.QUIT:
            print("=======================================")
            input_data = input("Input Command (To quit, type 'q' or 'quit'): ")
            print()

            result = self.__process(input_data)
            if result is CommandProcessor.ReturnStatus.UNKNOWN:
                print("Unvalid Command: '{}'".format(input_data))
                print("Type 'h' or 'help' to show all commands")

        Logger().info("Program exit")
