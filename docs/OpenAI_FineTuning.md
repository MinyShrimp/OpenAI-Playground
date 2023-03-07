# Fine-Tuning - 미세 조정

## 소개

> 사전 학습 데이터를 기준으로 새로운 프롬프트의 값을 추출하는 기법 - [미세 조정 가이드](https://platform.openai.com/docs/guides/fine-tuning)

OpenAPI 가 제공하는 API 대신 GPT-3 을 사용하여 자신의 어플리케이션에 맞게 모델을 미세 조정하는 기능입니다.
GTP-3.5 출시 이전에 사용되던 GPT-3 을 사용하기 때문에 사전에 개방형 인터넷에서 훈련된 모델에
사용자가 원하는 데이터를 입력하여 자신의 어플리케이션에 특화된 데이터를 얻어낼 수 있게 됩니다.

### Fine Tuning 을 위한 단계

* 학습 데이터 준비 및 업로드
* 미세 조정된 새 모델 학습
* 미세 조정된 모델 사용

### 장점

* 높은 결과 품질
* 프롬프트에 입력하는 것 보다 더 많은 예제를 학습할 수 있는 능력
* 짧은 프롬프트로 인한 비용 절약
* 낮은 요청 대기 시간

정리하자면 미세 조정이 완료된 모델은 프롬프트에 예제를 제공하지 않아도 답을 얻을 수 있으며,
이로 인해 기존의 API 를 사용하는 것보다 절감된 비용과 빠른 응답 속도를 얻을 수 있습니다.

### 지원 모델 목록

현재 Fine Tuning 을 사용할 수 있는 모델은 다음과 같습니다.

* Davinci
* Curie
* Babbage
* Ada

## 훈련 데이터 준비

### 필수 조건

Fine Tuning 에 사용되는 데이터는 아래의 조건을 만족해야 합니다.

* JSONL (Json Lines) 문서
* `prompt` - `completion` 키 쌍으로 이루어진 Json 데이터
    * `{"prompt": "prompt text", "completion": "ideal generated text"}`

### 만족하면 좋은 조건

필수는 아니지만 아래의 조건을 만족하면 더 좋은 결과를 얻을 수 있습니다.

* 각 Prompt 데이터는 고정된 구분 기호 (`\n\n###\n\n`) 로 끝나면 좋습니다.
    * 구분 기호는 Prompt 에 포함되지 않은 기호로 해야합니다.
* Completion 데이터는 공백 (` `) 으로 시작하면 좋습니다.
    * GPT 모델 들은 [Tokenizer](https://platform.openai.com/tokenizer)을 사용하여 텍스트를 처리합니다.
    * 위 링크를 접속하면 Tokenizer 의 작동 방식을 확인할 수 있습니다.

### CLI 데이터 준비 도구

```shell
$ openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
```

## Files

> [Files Document](https://platform.openai.com/docs/api-reference/files)

Files 는 Fine Tuning 에 사용할 파일을 업로드하는데 사용됩니다.

### 업로드된 파일 얻기

#### HTTP API

```shell
curl https://api.openai.com/v1/files \
  -X GET \
  -H 'Authorization: Bearer OPENAI_API_KEY'
```

#### Python

```Python
import os
import openai

ai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.list()
```

#### 결과

```json
{
    "data": [
        {
            "bytes": 60800,
            "created_at": 1678202345,
            "filename": "data/data_train.jsonl",
            "id": "file-XXXXX",
            "object": "file",
            "purpose": "fine-tune",
            "status": "processed",
            "status_details": null
        }
    ],
    "object": "list"
}
```

### 파일 업로드

#### HTTP API

```shell
curl https://api.openai.com/v1/files \
  -X POST \
  -H "Authorization: Bearer OPENAI_API_KEY" \
  -F purpose="fine-tune" \
  -F file='@mydata.jsonl'
```

#### Python

```Python
import os
import openai

from typing import TextIO

ai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.create(
    purpose=purpose,
    file=open("data/prepared_train.jsonl")
)
```

| Key       | 뜻                  | 필수     | 설명                                       |
|-----------|--------------------|--------|------------------------------------------|
| `purpose` | 업로드의 목적            | `true` | Fine Tuning 이 목적이면 `fine-tune` 을 입력합니다.  |
| `file`    | 업로드할 JSON Lines 파일 | `true` | `prompt`, `completion` field 를 포함해야 합니다. |

#### Response

```json
{
    "bytes": 60800,
    "created_at": 1678207868,
    "filename": "file",
    "id": "file-XXX",
    "object": "file",
    "purpose": "fine-tune",
    "status": "uploaded",
    "status_details": null
}
```

### 파일 삭제

#### HTTP API

```shell
curl https://api.openai.com/v1/files/{file_id} \
  -X DELETE \
  -H 'Authorization: Bearer OPENAI_API_KEY'
```

#### Python

```Python
import os
import openai

ai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.download(
    id=file_id
)
```

| Query String | 뜻          | 필수     | 설명                      |
|--------------|------------|--------|-------------------------|
| `{file_id}`  | 업로드된 파일 ID | `true` | 삭제할 파일 ID 를 포함하여 요청합니다. |

#### Response

```json
{
    "deleted": true,
    "id": "file-XXXXX",
    "object": "file"
}
```

### 파일 검색

#### HTTP API

```shell
curl https://api.openai.com/v1/files/{file_id} \
  -X GET \
  -H 'Authorization: Bearer OPENAI_API_KEY'
```

#### Python

```python
import os
import openai
from openai import util
from openai.api_requestor import APIRequestor

ai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

requestor = APIRequestor()
response, _, api_key = requestor.request(
    method="get",
    url="/files/{}".format(file_id)
)

util.convert_to_openai_object(
    response, api_key, None, None
)
```

| Query String | 뜻          | 필수     | 설명                   |
|--------------|------------|--------|----------------------|
| `{file_id}`  | 업로드된 파일 ID | `true` | 특정 파일에 대한 정보를 반환합니다. |

#### Response

```json
{
    "bytes": 60800,
    "created_at": 1678207868,
    "filename": "file",
    "id": "file-XXXXX",
    "object": "file",
    "purpose": "fine-tune",
    "status": "processed",
    "status_details": null
}
```

### 파일 내용 검색

#### HTTP API

```shell
curl https://api.openai.com/v1/files/{file_id}/content \
  -X GET \
  -H 'Authorization: Bearer OPENAI_API_KEY' \
  > file.jsonl
```

#### Python

```Python
import os
import openai

ai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.download(
    id=file_id
)
```

| Query String | 뜻          | 필수     | 설명                |
|--------------|------------|--------|-------------------|
| `{file_id}`  | 업로드된 파일 ID | `true` | 특정 파일의 내용을 반환합니다. |

#### Response

* `openai.error.InvalidRequestError`: 무료 계정은 다운로드가 불가능합니다.

## Fine Tuning

### HTTP API

```shell
curl https://api.openai.com/v1/fine-tunes \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer OPENAI_API_KEY" \
  -d '{"training_file": "{file_id}"}'
```

### Python

```Python

```