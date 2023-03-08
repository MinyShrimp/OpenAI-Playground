from common import CommandProcessor
from common import EnvLoader
from common import Logger


def init():
    EnvLoader.load()
    log = Logger()
    log.info("Hello, Welcome to My Program !!!")


def run():
    processor = CommandProcessor()
    processor.process()


if __name__ == '__main__':
    init()
    run()
