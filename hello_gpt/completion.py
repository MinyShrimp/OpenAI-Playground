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
            prompt: str
    ):
        return openai.Completion.create(
            model=model_id,
            prompt=prompt
        )
