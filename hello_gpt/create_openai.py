import os
import openai
from common import EnvLoader


def create() -> None:
    EnvLoader.load()
    openai.api_key = os.getenv("OPEN_AI_KEY")
    print(openai.api_key)
