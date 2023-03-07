import os

import openai

from common import EnvLoader


def create() -> None:
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(openai.api_key)
