from common import log
from common import EnvLoader
from common import measure
from commands import CommandProcessor

from hello_gpt import Moderation


def cmd_proxy_factory(gpt_proxy):
    def measure_proxy(target, **kwargs):
        result = measure(target, **kwargs)
        log.debug(result)
        print(result)
        return CommandProcessor.ReturnStatus.OK

    return lambda **kwargs: measure_proxy(gpt_proxy, **kwargs)


def init():
    EnvLoader.load()
    CommandProcessor().add_command("m", {
        "description": "Moderation Prompt",
        "supports": ["mo", "moderation"],
        "do": cmd_proxy_factory(Moderation.call),
    })


def run():
    CommandProcessor().process()


if __name__ == '__main__':
    init()
    run()
