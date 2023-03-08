from common import log
from common import measure
from . import CommandProcessor

'''
Since: 2023-03-09
Author: 김회민 ksk7584@gmail.com
'''


def cmd_proxy_factory(gpt_proxy):
    def measure_proxy(target, **kwargs):
        result = measure(target, **kwargs)
        log.debug(result)
        return CommandProcessor.ReturnStatus.OK

    return lambda **kwargs: measure_proxy(gpt_proxy, **kwargs)
