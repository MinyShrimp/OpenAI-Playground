from typing import Union

import openai

from cmds import CommandUtils
from .completion_view import CompletionView

"""
Since: 2023-03-11
Author: 김회민 ksk7584@gmail.com
"""


class Completion:

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["c", "completion"],
        description="Create Completion",
        view_func=CompletionView.create_view
    )
    def create(
            model_id: str,
            prompt: str,
            suffix: str = None,
            max_tokens: int = 100,
            temperature: float = 1,
            top_p: float = 1,
            n: int = 1,
            stream: bool = False,
            logprobs: int = None,
            echo: bool = False,
            stop: Union[str, list] = None,
            presence_penalty: float = 0,
            frequency_penalty: float = 0,
            best_of: int = 1
    ):
        return openai.Completion.create(
            model=model_id,
            prompt=prompt,
            suffix=suffix,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stream=stream,
            logprobs=logprobs,
            echo=echo,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            best_of=best_of
        )
