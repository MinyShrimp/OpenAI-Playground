from enum import Enum

from common.multi_key_dict import MultiKeyDict

'''
Since: 2023-03-08
Author: 김회민 ksk7584@gmail.com
'''


class CommandProcessor(object):
    """ 명령어 처리 클래스

    Singleton 패턴 적용: CommandProcessor()
    """
    __INSTANCE = None
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
    __COMMANDS_MULTI = MultiKeyDict()
    __COMMANDS_DECS = []

    @staticmethod
    class ReturnStatus(Enum):
        OK = 1
        QUIT = -1
        UNKNOWN = 0

    def __init__(self):
        self.__COMMANDS["h"]["do"] = self.__help_do
        self.__COMMANDS["q"]["do"] = self.__quit_do

        self.__COMMANDS_MULTI.bulk_add(self.__COMMANDS)
        self.__COMMANDS_DECS = [
            "- '{}': {}".format(
                "' or '".join(key),
                value["description"]
            ) for key, value in self.__COMMANDS_MULTI.items()
        ]

    def __new__(cls):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(CommandProcessor, cls).__new__(cls)
        return cls.__INSTANCE

    def __help_do(self) -> ReturnStatus:
        print("commands list")
        for desc in self.__COMMANDS_DECS:
            print(desc)
        return CommandProcessor.ReturnStatus.OK

    @staticmethod
    def __quit_do() -> ReturnStatus:
        print("Good bye")
        return CommandProcessor.ReturnStatus.QUIT

    def __process(self, command: str) -> ReturnStatus:
        command = command.replace("\n", "").strip()
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
