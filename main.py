import os

import openai

from commands import CommandProcessor
from common import EnvLoader


def init():
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")


if __name__ == '__main__':
    init()
    processor = CommandProcessor()
    processor.process()
