import openai

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com
'''


class Moderation:

    @staticmethod
    def call():
        """ 해당 요청에 대한 검증

        :return: docs/OpenAI_Moderation.md 참고
        """
        return openai.Moderation.create(
            model="text-moderation-latest",
            input=["I want to kill them.", "I love you"]
        )
