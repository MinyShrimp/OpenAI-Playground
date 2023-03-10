from pandas import DataFrame

"""
Since: 2023-03-10
Author: 김회민 ksk7584@gmail.com
"""


class GeneralView:

    @staticmethod
    def _get_fine_tune_job(datas: list):
        df = DataFrame(datas)
        df.set_index("id", inplace=True)
        return df

    @staticmethod
    def _print_list(datas: DataFrame):
        if len(datas) == 0:
            print("Empty")
        else:
            print(datas)

    @classmethod
    def list_view(cls, response: list):
        cls._print_list(cls._get_fine_tune_job(response))
        return response

    @classmethod
    def item_view(cls, response: dict):
        cls._print_list(cls._get_fine_tune_job([response]))
        return response
