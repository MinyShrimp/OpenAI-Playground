from typing import TextIO

import openai

'''
Since: 2023-03-08
Author: 김회민 ksk7584@gmail.com
'''


class Files:

    @staticmethod
    def get_file_list() -> list:
        """ 업로드된 모든 파일 List

        :return: 업로드된 모든 파일 List
        """
        return openai.File.list()["data"]

    @staticmethod
    def upload_file(file: TextIO, purpose: str = "fine-tune"):
        """ 파일 업로드

        :param file: open("file_path")
        :param purpose: "fine-tune"
        :return: 파일 정보
        """
        return openai.File.create(
            purpose=purpose,
            file=file,
            user_provided_filename=file.name
        )

    @staticmethod
    def search_file(file_id: str):
        """ File ID 기반 검색

        :param file_id: 업로드된 File ID
        :return: 파일 정보
        """
        return openai.File.retrieve(
            id=file_id
        )

    @staticmethod
    def download_file(file_id: str):
        """ Fine-Tuning File 다운로드

        :param file_id: OpenAI 에 업로드된 File ID
        :raise openai.error.InvalidRequestError: 무료 계정은 다운로드가 불가능합니다.
        """
        return openai.File.download(
            id=file_id,
        )

    @staticmethod
    def delete_file(file_id: str):
        """ 업로드된 파일 제거

        :param file_id: OpenAI 에 업로드된 File 의 ID
        :return: { "deleted": true, "id": "file-XXXXX", "object": "file" }
        """
        return openai.File.delete(
            sid=file_id
        )