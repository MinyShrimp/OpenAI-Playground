from common import CommandProcessor
from common import EnvLoader


def init():
    EnvLoader.load()


def run():
    processor = CommandProcessor()
    processor.process()


if __name__ == '__main__':
    init()
    run()
