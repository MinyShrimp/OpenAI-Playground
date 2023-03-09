from typing import Callable

from common import log
from common import measure
from . import CommandProcessor

'''
Since: 2023-03-09
Author: 김회민 ksk7584@gmail.com
'''


class CommandUtils:
    __processor = CommandProcessor()

    @staticmethod
    def cmd_proxy_factory(gpt_proxy):
        def measure_proxy(target, **kwargs):
            result = measure(target, **kwargs)
            log.debug(result)
            return CommandProcessor.ReturnStatus.OK

        return lambda **kwargs: measure_proxy(gpt_proxy, **kwargs)

    @classmethod
    def add_helper(
            cls,
            key: str,
            description: str,
            do: Callable,
            supports: list[str]
    ):
        cls.__processor.add_command(key, {
            "description": description,
            "do": cls.cmd_proxy_factory(do),
            "supports": supports if supports is not None else []
        })
