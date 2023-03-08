from common import EnvLoader

from commands import CommandProcessor


def init():
    EnvLoader.load()


def run():
    processor = CommandProcessor()
    processor.process()


if __name__ == '__main__':
    init()
    run()
