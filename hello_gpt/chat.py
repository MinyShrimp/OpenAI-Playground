import openai

from common import log
from cmds import CommandUtils

"""
Since: 2023-03-11
Author: 김회민 ksk7584@gmail.com
"""


class Chat:

    @staticmethod
    def __send_message(
            msg: str,
            model_id: str
    ):
        return openai.ChatCompletion.create(
            model=model_id,
            messages=[{"role": "user", "content": msg}]
        )

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["cs", "chat start"],
        description="Start Chat"
    )
    def create(
            model_id: str = "gpt-3.5-turbo"
    ):
        log.info(f"{model_id} 와의 채팅을 시작합니다.")
        while True:
            u_msg = input("User   : ")
            u_msg = u_msg.strip()
            if u_msg == 'q' or u_msg == 'quit':
                break
            if u_msg == "":
                continue

            response = Chat.__send_message(u_msg, model_id)
            a_msg = response['choices'][0]['message']['content']
            a_msg = a_msg.replace(".", ".\n")
            print(f"OpenAI : {a_msg}")

            log.debug('User: %s', u_msg)
            log.debug(response)

        log.info("채팅을 종료합니다.")
