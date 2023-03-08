import os

import dotenv
import openai

from . import Logger

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com

# 사용법

from common import EnvLoader

EnvLoader.load()
'''


class EnvLoader:
    """환경 설정 파일을 로드합니다.
    """

    @classmethod
    def __load_env(cls) -> None:
        return os.getenv("OPENAI_API_KEY") is not None

    @classmethod
    def load(cls) -> None:
        """Load OPENAI_API_KEY

        * .env 에 저장된 환경 설정에 OPENAI_API_KEY 가 있는지 확인
        * 없다면 해당 폴더에 .env 파일을 불러와 확인
        * OPENAI_API_KEY 의 값이 어느 곳에도 없으면 예외

        :raise 환경 설정에서 OPENAI_API_KEY 가 없다면 예외가 발생됩니다.
        """
        log = Logger()

        if cls.__load_env() is False:
            dotenv.load_dotenv()
            if cls.__load_env() is False:
                log.error("Not Found OPENAI_API_KEY")
                raise Exception("OPENAI_API_KEY 의 설정을 확인할 수 없습니다.")

        openai.api_key = os.getenv("OPENAI_API_KEY")
        log.debug("OPENAI_API_KEY: [%s]", openai.api_key)
