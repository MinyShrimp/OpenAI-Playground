import os

import openai

from common import EnvLoader, measure
from hello_gpt.fine_tuning_file import Files

if __name__ == '__main__':
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # result = measure(moderation.moderation_test)

    file_list = measure(Files.get_file_list)
    print(file_list)
    # result = measure(lambda: Files.delete_file(file_list[0]["id"]))
    # print(result)

    # upload_result = measure(
    #     lambda: Files.upload_file(
    #         file=open("data/prepared_train.jsonl")
    #     )
    # )
    # print(upload_result)

    search_result = measure(
        lambda: Files.search_file(
            file_id=file_list[0]["id"]
        )
    )
    print(search_result)
