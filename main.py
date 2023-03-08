from common import EnvLoader
from cmds import CommandProcessor
from hello_gpt import GptConfig


def init():
    EnvLoader.load()
    GptConfig.config()


def run():
    CommandProcessor().process()


if __name__ == '__main__':
    init()
    run()
