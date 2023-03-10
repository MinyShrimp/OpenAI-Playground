import inspect
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

        def cmd_proxy(**kwargs):
            sig = inspect.signature(gpt_proxy)
            bound_args = sig.bind(**kwargs)
            bound_args.apply_defaults()

            for param_name, param_value in bound_args.arguments.items():
                target_param_type = sig.parameters[param_name].annotation
                if target_param_type is str:
                    kwargs[param_name] = "".join(kwargs[param_name])
                    log.debug("trans result - %s", kwargs[param_name])

            return measure_proxy(gpt_proxy, **kwargs)

        return cmd_proxy

    @classmethod
    def add_helper(
            cls,
            keys: list[str],
            description: str,
            do: Callable
    ):
        cls.__processor.add_command(keys, {
            "description": description,
            "do": cls.cmd_proxy_factory(do)
        })
