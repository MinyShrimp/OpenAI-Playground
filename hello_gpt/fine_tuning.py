from os import system
import subprocess
from requests.exceptions import ChunkedEncodingError

import openai

from common import log
from cmds import CommandUtils
from .fine_tuning_view import FineTuneView

'''
Since: 2023-03-08
Author: 김회민 ksk7584@gmail.com
'''


class FineTuning:

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["pd", "prepare create"],
        description="Create Fine-Tune Prepare data"
    )
    def create_prepare_file(
            file_name: str
    ):
        _cmd = f"openai tools fine_tunes.prepare_data -f {file_name}"
        return subprocess.run(_cmd.split(' '))

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ftcr", "fine create"],
        description="Create Fine-Tuning Model",
        view_func=FineTuneView.create_view
    )
    def create_fine_tune(
            train_file_id: str,
            validation_file_id: str = None,
            model_name: str = "curie"
    ):
        """ 업로드한 파일을 이용하여 새로운 Fine-Tune Model 을 생성합니다.

        POST https://api.openai.com/v1/fine-tunes

        :param train_file_id: xxx_train.jsonl
        :param validation_file_id: (optional) xxx_valid.jsonl
        :param model_name: Fine-Tunes 의 Base Model 이름. ada, babbage, curie, davinci
        :return:
        """
        return openai.FineTune.create(
            training_file=train_file_id,
            validation_file=validation_file_id,
            model=model_name
        )

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ftcc", "fine cancel"],
        description="Cancel Fine-Tuning Job",
        view_func=FineTuneView.cancel_view
    )
    def cancel_fine_tune(
            fine_tune_id: str
    ):
        """ 진행중인 Fine-Tune 생성을 중지합니다.

        POST https://api.openai.com/v1/fine-tunes/{fine_tune_id}/cancel

        :param fine_tune_id: 생성 진행 중인 Fine-Tune ID
        :return: { Fine-Tune 정보 }
        """
        return openai.FineTune.cancel(
            id=fine_tune_id
        )

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ftst", "fine stream"],
        description="Stream Creating Fine-Tuning Job"
    )
    def stream_fine_tune(
            fine_tune_id: str
    ):
        _jobs = []
        print("Stream Fine-Tune Job...")
        while True:
            try:
                stream = openai.FineTune.stream_events(
                    id=fine_tune_id
                )

                for i, v in enumerate(stream):
                    msg = v["message"]
                    if i >= len(_jobs):
                        _jobs.append(msg)
                        print(msg)
                        log.debug(msg)
                    if msg == "Fine-tune succeeded":
                        return _jobs
            except ChunkedEncodingError as e:
                log.warning(e)

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ftl", "fine list"],
        description="Get All Creating Fine-Tune Jobs",
        view_func=FineTuneView.list_view
    )
    def get_list():
        """ Fine-Tunes Model List

        GET https://api.openai.com/v1/fine-tunes

        :return: [ { Fine-Tune 정보 } ] }
        """
        return openai.FineTune.list()["data"]

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fts", "fine search"],
        description="Search Creating Fine-Tune Job",
        view_func=FineTuneView.item_view
    )
    def get_one(
            fine_tune_id: str
    ):
        """ Fine-Tune 단일 조회

        GET https://api.openai.com/v1/fine-tunes/{fine_tune_id}

        :param fine_tune_id: 조회를 원하는 Fine-Tune ID
        :return: { Fine-Tune 정보 }
        """
        return openai.FineTune.retrieve(
            id=fine_tune_id
        )

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fte", "fine event"],
        description="Get Creating Fine-Tune Job Events",
        view_func=FineTuneView.events_view
    )
    def get_one_events(
            fine_tune_id: str
    ) -> list:
        """ 해당 Fine-Tune 의 이벤트 목록 조회

        GET https://api.openai.com/v1/fine-tunes/{fine_tune_id}/events

        :param fine_tune_id: 조회를 원하는 Fine-Tune ID
        :return: list 형태로 반환
        """
        return openai.FineTune.retrieve(
            id=fine_tune_id
        )["events"]

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ftd", "fine delete"],
        description="Delete Created Fine-Tune Model",
    )
    def delete_model(
            model_id: str,
            model_name: str = "curie"
    ):
        """ Delete Fine-Tune Model

        DELETE https://api.openai.com/v1/models/{model}

        :param model_id: 삭제를 원하는 Fine-Tune ID
        :param model_name: Fine-Tune Model 에 사용한 원본 모델 이름
        :raise openai.error.InvalidRequestError: 모델이 존재하지 않습니다.
        :return:
        """
        return openai.Model.delete(
            sid="{}:{}".format(model_name, model_id)
        )
