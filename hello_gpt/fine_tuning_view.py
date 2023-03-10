from pandas import DataFrame
from .general_view import GeneralView

"""
Since: 2023-03-10
Author: 김회민 ksk7584@gmail.com
"""


class FineTuneView(GeneralView):

    @staticmethod
    def _get_fine_tune_job(datas: list):
        df = DataFrame([{
            "id": r["id"],
            "model": r["model"],
            "object": r["object"],
            "organization_id": r["organization_id"],
            "training_files": [_["id"] for _ in r["training_files"]],
            "validation_files": [_["id"] for _ in r["validation_files"]],
            "result_files": [_["id"] for _ in r["result_files"]],
            "created_at": r["created_at"],
            "updated_at": r["updated_at"],
            "status": r["status"],
            "fine_tuned_model": r["fine_tuned_model"]
        } for r in datas])
        df.set_index("id", inplace=True)
        return df

    @staticmethod
    def __show_desc(fine_tune_id: str):
        print(f"check for [fts -fine_tune_id \"{fine_tune_id}\"].")
        print(f"check details for [fte -fine_tune_id \"{fine_tune_id}\"]].")

    @classmethod
    def create_view(cls, response: dict):
        print("Start Creating Fine-Tune Job.")
        cls.__show_desc(response['id'])
        return cls.item_view(response)

    @classmethod
    def cancel_view(cls, response: dict):
        print("Cancel Fine-Tune Job.")
        cls.__show_desc(response['id'])
        return cls.item_view(response)

    @classmethod
    def events_view(cls, response: list):
        cls._print_list(DataFrame(response))
        return response
