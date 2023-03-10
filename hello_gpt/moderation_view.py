from pandas import DataFrame


class ModerationView:
    """
    Since: 2023-03-09
    Author: 김회민 ksk7584@gmail.com
    """

    @staticmethod
    def view(response: dict):
        results = response["results"]

        print("======= Moderation Result =======")
        print(f"Model Name: [{response['model']}]")
        categories = {}
        for result in results:
            categories[result["value"]] = {"result": result["flagged"], **result["categories"]}

        print(DataFrame(categories))
        return response
