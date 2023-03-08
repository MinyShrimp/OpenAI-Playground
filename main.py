import os

import openai

from common import CommandProcessor, EnvLoader

if __name__ == '__main__':
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    processor = CommandProcessor()
    processor.process()
