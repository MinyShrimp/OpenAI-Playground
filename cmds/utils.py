import inspect
from typing import Callable
from functools import wraps

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
    def cmd_proxy_factory(gpt_proxy, gpt_view_proxy):
        def measure_proxy(**kwargs):
            result = measure(gpt_proxy, **kwargs)
            if gpt_view_proxy is not None:
                gpt_view_proxy(result)
            log.debug("[%s.%s] result = %s", gpt_proxy.__module__, gpt_proxy.__name__, result)
            return CommandProcessor.ReturnStatus.OK

        @wraps(gpt_proxy)
        def cmd_proxy(**kwargs):
            sig = inspect.signature(gpt_proxy)
            bound_args = sig.bind(**kwargs)

            for param_name, param_value in bound_args.arguments.items():
                target_param_type = sig.parameters[param_name].annotation
                if target_param_type is str:
                    kwargs[param_name] = kwargs[param_name][0]
                    log.debug(
                        "[%s.%s] trans '%s' param = %s",
                        gpt_proxy.__module__, gpt_proxy.__name__,
                        param_name, kwargs[param_name]
                    )

            return measure_proxy(**kwargs)

        return cmd_proxy

    @classmethod
    def add_helper(
            cls,
            keys: list[str],
            description: str,
            do: Callable,
            view: Callable
    ):
        cls.__processor.add_command(keys, {
            "description": description,
            "do": cls.cmd_proxy_factory(do, view)
        })

    @classmethod
    def add_decorator(
            cls,
            keys: list[str],
            description: str,
            view_func=None
    ):
        def __decorator(func):
            cls.add_helper(keys, description, do=func, view=view_func)

        return __decorator
