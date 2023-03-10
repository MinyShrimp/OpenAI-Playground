import openai

from cmds import CommandUtils
from .moderation_view import ModerationView

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com
'''


class Moderation:

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["m", "mo", "moderation"],
        description="Moderation Prompt",
        view_func=ModerationView.view
    )
    def check_value(inputs: list):
        """ 해당 요청에 대한 검증

        :param inputs: 검증을 원하는 데이터
        :return: docs/OpenAI_Moderation.md 참고
        """

        response = openai.Moderation.create(
            model="text-moderation-latest",
            input=inputs
        )

        for _input, result in zip(inputs, response["results"]):
            result["value"] = _input

        return response
