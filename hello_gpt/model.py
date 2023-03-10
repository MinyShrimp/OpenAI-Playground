import openai

from cmds import CommandUtils
from .general_view import GeneralView


class Model:
    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ml", "model list"],
        description="Get All Models List",
        view_func=GeneralView.list_view
    )
    def get_all_list():
        """ 모든 모델 리스트
        """
        return openai.Model.list()["data"]

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["ms", "model search"],
        description="Get Model",
        view_func=GeneralView.item_view
    )
    def get_one_model(
            model_id: str
    ):
        return openai.Model.retrieve(
            id=model_id
        )

    @staticmethod
    @CommandUtils.add_decorator(
        keys=["msp", "model search permissions"],
        description="Get Permissions of Model",
        view_func=GeneralView.list_view
    )
    def get_permissions(
            model_id: str
    ):
        return openai.Model.retrieve(
            id=model_id
        )["permission"]
