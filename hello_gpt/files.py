import openai
from openai import InvalidRequestError

from common import log
from cmds import CommandUtils
from .general_view import GeneralView

'''
Since: 2023-03-08
Author: 김회민 ksk7584@gmail.com
'''


class Files:

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fl", "file list"],
        description="Get All File List",
        view_func=GeneralView.list_view
    )
    def get_file_list() -> list:
        """ 업로드된 모든 파일 List

        :return: 업로드된 모든 파일 List
        """
        return openai.File.list()["data"]

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fu", "file upload"],
        description="Upload File",
        view_func=GeneralView.list_view
    )
    def upload_file(
            files: list,
            purpose: str = "fine-tune"
    ):
        """ 파일 업로드

        :param files: 파일 이름들
        :param purpose: "fine-tune"
        :return: 파일 정보
        """
        result = []
        for file in files:
            try:
                with open(file, "r") as f:
                    result.append(
                        openai.File.create(
                            purpose=purpose,
                            file=f,
                            user_provided_filename=file
                        )
                    )
            except InvalidRequestError:
                log.warning(f"JSONL 파일만 업로드 가능합니다. {file}은 무시됩니다.")
        return result

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fs", "file search"],
        description="Search File",
        view_func=GeneralView.item_view
    )
    def search_file(file_id: str):
        """ File ID 기반 검색

        :param file_id: 업로드된 File ID
        :return: 파일 정보
        """
        return openai.File.retrieve(
            id=file_id
        )

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fdo", "file download"],
        description="Download File",
    )
    def download_file(
            file_id: str,
            file_name: str = None
    ):
        """ Fine-Tuning File 다운로드

        :param file_id: OpenAI 에 업로드된 File ID
        :param file_name:
        :raise openai.error.InvalidRequestError: 무료 계정은 다운로드가 불가능합니다.
        """

        response = openai.File.download(
            id=file_id,
        )

        if file_name is None:
            file_name = openai.File.retrieve(file_id)["filename"]

        with open(file_name, "wb") as f:
            f.write(response)

        print(f"Completed Download File: {file_name}")
        return {"file_name": file_name}

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["fde", "file delete"],
        description="Delete File",
        view_func=GeneralView.item_view
    )
    def delete_file(file_id: str):
        """ 업로드된 파일 제거

        :param file_id: OpenAI 에 업로드된 File 의 ID
        :return: { "deleted": true, "id": "file-XXXXX", "object": "file" }
        """
        return openai.File.delete(
            sid=file_id
        )
