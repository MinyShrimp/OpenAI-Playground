from cmds import CommandUtils

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
        CommandUtils.add_helper(
            key="m",
            description="Moderation Prompt",
            supports=["mo", "moderation"],
            do=Moderation.call
        )

        # File
        CommandUtils.add_helper(
            key="fl",
            description="Get File List",
            supports=["file list"],
            do=Files.get_file_list
        )
