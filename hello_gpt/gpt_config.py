from cmds import CommandProcessor
from cmds import ProxyFactory

from hello_gpt import Moderation
from hello_gpt import Files

'''
Since: 2023-03-09
Author: 김회민 ksk7584@gmail.com
'''


class GptConfig:

    @staticmethod
    def config():
        # Moderation
        CommandProcessor().add_command("m", {
            "description": "Moderation Prompt",
            "supports": ["mo", "moderation"],
            "do": ProxyFactory(Moderation.call),
        })

        # File
        CommandProcessor().add_command("file list", {
            "description": "Get File List",
            "supports": ["fl"],
            "do": ProxyFactory(Files.get_file_list),
        })
