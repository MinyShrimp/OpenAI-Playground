import openai

from common import log
from hello_gpt import ModerationView

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com
'''


class Moderation:

    @staticmethod
    def call(inputs: list[str]):
        """ 해당 요청에 대한 검증

        :param inputs: 검증을 원하는 데이터
        :return: docs/OpenAI_Moderation.md 참고
        """

        log.info("Moderation Targets : %s", inputs)

        response = openai.Moderation.create(
            model="text-moderation-latest",
            input=inputs
        )

        log.debug("Moderation Response : %s", response)
        ModerationView.view(inputs, response)
        return response
