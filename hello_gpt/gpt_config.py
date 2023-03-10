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
            keys=["m", "mo", "moderation"],
            description="Moderation Prompt - Option: '-inputs \"Hello World\"'",
            do=Moderation.call
        )

        # File
        CommandUtils.add_helper(
            keys=["fl", "file list"],
            description="Get All File List",
            do=Files.get_file_list
        )

        CommandUtils.add_helper(
            keys=["fs", "file search"],
            description="Search One File",
            do=Files.search_file
        )
