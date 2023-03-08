# Fine-Tuning APIs

해당 문서는 [공식 Document](https://platform.openai.com/docs/api-reference/files) 를 참고하여 작성한 내용이 담겨 있습니다.

그 외에도 python 의 openai 라이브러리를 사용하는 방법과 그에 따른 결과물도 소개합니다.

## Files

> [Files Document](https://platform.openai.com/docs/api-reference/files)

Files 는 Fine-Tuning 에 사용할 파일을 업로드하는데 사용됩니다.

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