import os

import openai

from common import EnvLoader
from hello_gpt.fine_tuning import FineTuning

if __name__ == '__main__':
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    result = FineTuning.delete_model(
        model_id="ft-GWBs2bIOdMwZ1QVQKVFgLbpX",
        model_name="ada"
    )
    print(result)
