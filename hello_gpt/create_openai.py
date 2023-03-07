import os

import openai

from common import EnvLoader

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com
'''


def create() -> None:
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(openai.api_key)
