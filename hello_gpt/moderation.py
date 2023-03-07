import os

import openai

from common import EnvLoader

'''
Since: 2023-03-07
Author: 김회민 ksk7584@gmail.com

{
    "id": "modr-XXXXX",
    "model": "text-moderation-004",
    "results": [
        {
            "categories": {
                "hate": false,
                "hate/threatening": false,
                "self-harm": false,
                "sexual": false,
                "sexual/minors": false,
                "violence": true,
                "violence/graphic": false
            },
            "category_scores": {
                "hate": 0.180674210190773,
                "hate/threatening": 0.003288434585556388,
                "self-harm": 1.8088556208439854e-09,
                "sexual": 9.759669410414062e-07,
                "sexual/minors": 1.3363569806301712e-08,
                "violence": 0.8864424824714661,
                "violence/graphic": 3.2010063932830235e-08
            },
            "flagged": true
        },
        {
            "categories": {
                "hate": false,
                "hate/threatening": false,
                "self-harm": false,
                "sexual": false,
                "sexual/minors": false,
                "violence": false,
                "violence/graphic": false
            },
            "category_scores": {
                "hate": 1.879640088020551e-08,
                "hate/threatening": 2.993451298470562e-13,
                "self-harm": 1.355260764723809e-10,
                "sexual": 5.208510992815718e-05,
                "sexual/minors": 2.207701221834668e-08,
                "violence": 2.5162718575444387e-09,
                "violence/graphic": 3.929976483130204e-11
            },
            "flagged": false
        }
    ]
}
'''


def moderation_test() -> None:
    EnvLoader.load()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Moderation.create(
        model="text-moderation-latest",
        input=["I want to kill them.", "I love you"]
    )
    print(response)
