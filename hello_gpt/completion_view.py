from pandas import DataFrame
from .general_view import GeneralView

"""
Since: 2023-03-11
Author: 김회민 ksk7584@gmail.com
"""


class CompletionView(GeneralView):

    @classmethod
    def create_view(cls, response: dict):
        _tmp = {**response}
        choices = _tmp.pop("choices")
        usage = _tmp.pop("usage")

        df = DataFrame(choices)
        df.set_index("index", inplace=True)

        print(choices[0]["text"])
        print("=======================================")
        cls.item_view(_tmp)
        print()
        cls._print_list(df)
        print()
        cls.item_view({"id": response["id"], **usage})
        return response
