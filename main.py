from common import EnvLoader
from cmds import CommandProcessor
from hello_gpt import *


def init():
    EnvLoader.load()


def run():
    CommandProcessor().process()


if __name__ == '__main__':
    init()
    run()
