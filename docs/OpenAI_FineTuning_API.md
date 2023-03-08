# Fine-Tuning APIs

해당 문서는 [공식 Document](https://platform.openai.com/docs/api-reference) 를 참고하여 작성한 내용이 담겨 있습니다.

그 외에도 python 의 openai 라이브러리를 사용하는 방법과 그에 따른 결과물도 소개합니다.

만약 Fine-Tuning 에 대한 자세한 설명을 원한다면 [Fine-Tuning 소개](OpenAI_FineTuning.md) 를 확인해주세요.

## Files

> [Files Document](https://platform.openai.com/docs/api-reference/files)

Files 는 Fine-Tuning 에 사용할 파일을 업로드하는데 사용됩니다.

### 모든 파일 조회

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
            "filename": "data/prepared_train.jsonl",
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

openai.api_key = os.getenv("OPENAI_API_KEY")
return openai.File.retrieve(
    id=file_id
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

## Fine Tuning

> [Fine-Tunes API](https://platform.openai.com/docs/api-reference/fine-tunes)

### 생성

#### HTTP API

```shell
curl https://api.openai.com/v1/fine-tunes \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer OPENAI_API_KEY" \
  -d '{"training_file": "{file_id}"}'
```

#### Python

```Python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.create(
    training_file="file_id",
    model="model_name"
)
```

| Parameters                     | Type          | Default | Required | 뜻                        |
|--------------------------------|---------------|---------|----------|--------------------------|
| trainig_file                   | String        |         | true     | 업로드된 트레이닝 파일 ID          |
| validation_file                | String        |         | false    | 유효성 검사를 위한 파일 ID         |
| model                          | String        | curie   | false    | Fine-Tune 에 사용할 모델 이름    |
| n_epochs                       | Integer       | 4       | false    | 모델 교육을 위한 Epoch 횟수       |
| batch_size                     | Integer       | null    | false    | 배치 크기                    |
| learning_rate_multiplier       | Double(0 ~ 1) | null    | false    | 학습 속도                    |
| prompt_loss_weight             | Double(0 ~ 1) | 0.01    | false    | 프롬프트 손실 가중치              |
| compute_classification_metrics | Boolean       | false   | false    | 분류 지표 설정 여부              |
| classification_n_classes       | Integer       | null    | false    | 분류 클래스 갯수                |
| classification_positive_class  | String        | null    | false    | 양성 클래스 이름                |
| classification_betas           | Array         | null    | false    | Precision, Recall 가중치 설정 |
| suffix                         | String        | null    | false    | 모델 이름의 접미사 설정            |

<style>
.h5 {
font-size: 16px;
}
</style>

* <b class="h5">trainig_file</b>
    * 업로드된 트레이닝 파일 ID
    * `xxx_train.jsonl`
* <b class="h5">validation_file</b>
    * 유효성 검사를 위한 파일 ID
    * `xxx_valid.jsonl`
* <b class="h5">model</b>
    * Fine-Tune 에 사용할 모델 이름
    * 기본값은 `curie` 입니다.
    * ada, babbage, curie, davinci
* <b class="h5">n_epochs</b>
    * 모델 교육을 위한 Epoch 횟수
* <b class="h5">batch_size</b>
    * 배치 크기
    * 기본적으로 예제 수의 ~0.2% 로 구성되며 상한은 256 입니다.
* <b class="h5">learning_rate_multiplier</b>
    * 학습 속도
    * 최종 batch_size 에 따라 0.05, 0.1, 0.2 로 설정됩니다.
    * 0.02 ~ 0.2 범위의 값으로 설정하는 것을 권장합니다.
* <b class="h5">prompt_loss_weight</b>
    * 프롬프트 손실 가중치
    * 모델이 프롬프트를 생성하기 위해 얼마나 많이 학습하는지 제어합니다.
    * 값이 높을수록 더욱 정확한 결과를 얻을 수 있습니다.
* <b class="h5">compute_classification_metrics</b>
    * `compute_classification_metrics = false`
    * 분류 지표 설정 여부
    * validation_file 을 이용하여 각 Epoch 별로 정확도 및 F-1 점수 같은 분류 지표를 계산합니다.
* <b class="h5">classification_n_classes</b>
    * `classification_n_classes = 4`
    * 분류 클래스 갯수
    * 다중 클래스 분류를 진행할 때 몇 개의 클래스를 사용할지 설정합니다.
* <b class="h5">classification_positive_class</b>
    * `classification_positive_class = "1"`
    * 양성 클래스 이름
    * 이진 클래스 분류를 진행할 때 어떤 문자가 양성 클래스인지 설정합니다.
* <b class="h5">classification_betas</b>
    * `classification_betas = [1, 1]`
    * F1 점수 계산에서 사용하는 Precision, Recall 값의 가중치를 설정합니다.
    * 이진 클래스 분류를 진행할 때 추가 파라미터로 설정할 수 있습니다.
    * **Precision**
        * 양성 클래스 샘플 중 실제로 양성 클래스인 샘플의 비율
        * 배열의 첫 번째 인덱스에 입력합니다.
    * **Recall**
        * 실제 양성 클래스 중 모델이 정확히 예측한 양성 클래스의 비율
        * 배열의 두 번째 인덱스에 입력합니다.
    * 기본값은 `[1, 1]` 이며, 0 ~ 1 사이의 값을 입력하여 가중치를 설정할 수 있습니다.
* <b class="h5">suffix</b>
    * 생성이 완료된 Fine-Tunes Model 의 이름에 추가할 접미사를 설정합니다.
    * 최대 길이는 40 자입니다.
    * 예를 들어 `suffix="mine"` 으로 설정하면, `ada:ft-your-org:custom-2022-02-15-02-21-04` 와 같은 모델 이름이 생성됩니다.

#### Response

```json
{
    "created_at": 1678266902,
    "events": [
        {
            "created_at": 1678266902,
            "level": "info",
            "message": "Created fine-tune: ft-XXXXX",
            "object": "fine-tune-event"
        }
    ],
    "fine_tuned_model": null,
    "hyperparams": {
        "batch_size": null,
        "learning_rate_multiplier": null,
        "n_epochs": 4,
        "prompt_loss_weight": 0.01
    },
    "id": "ft-XXXXX",
    "model": "ada",
    "object": "fine-tune",
    "organization_id": "org-XXXXX",
    "result_files": [],
    "status": "pending",
    "training_files": [
        {
            "bytes": 60800,
            "created_at": 1678266670,
            "filename": "file",
            "id": "file-XXXXX",
            "object": "file",
            "purpose": "fine-tune",
            "status": "processed",
            "status_details": null
        }
    ],
    "updated_at": 1678266902,
    "validation_files": [
        {
            "bytes": 18712,
            "created_at": 1678266669,
            "filename": "file",
            "id": "file-XXXXX",
            "object": "file",
            "purpose": "fine-tune",
            "status": "processed",
            "status_details": null
        }
    ]
}
```

### 생성 중지

#### HTTP API

```shell
curl https://api.openai.com/v1/fine-tunes/{fine_tune_id}/cancel \
  -X POST \
  -H "Authorization: Bearer OPENAI_API_KEY"
```

#### Python

```Python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.cancel(
    id="fine_tune_id"
)
```

| Parameter        | 설명               |
|------------------|------------------|
| `{fine_tune_id}` | Fine-Tune Job ID |

#### Response

```json
{
    "created_at": 1678266902,
    "events": [
        {
            "created_at": 1678266902,
            "level": "info",
            "message": "Created fine-tune: ft-XXXXX",
            "object": "fine-tune-event"
        },
        {
            "created_at": 1678267042,
            "level": "info",
            "message": "Fine-tune cancelled",
            "object": "fine-tune-event"
        }
    ],
    "fine_tuned_model": null,
    "hyperparams": {
        "batch_size": null,
        "learning_rate_multiplier": null,
        "n_epochs": 4,
        "prompt_loss_weight": 0.01
    },
    "id": "ft-XXXXX",
    "model": "ada",
    "object": "fine-tune",
    "organization_id": "org-XXXXX",
    "result_files": [],
    "status": "cancelled",
    "training_files": [
        {
            "bytes": 60800,
            "created_at": 1678266670,
            "filename": "file",
            "id": "file-XXXXX",
            "object": "file",
            "purpose": "fine-tune",
            "status": "processed",
            "status_details": null
        }
    ],
    "updated_at": 1678267042,
    "validation_files": [
        {
            "bytes": 18712,
            "created_at": 1678266669,
            "filename": "file",
            "id": "file-XXXXX",
            "object": "file",
            "purpose": "fine-tune",
            "status": "processed",
            "status_details": null
        }
    ]
}
```

### 모든 Fine-Tunes Model 조회

#### HTTP API

```shell
curl https://api.openai.com/v1/fine-tunes \
  -X GET \
  -H 'Authorization: Bearer OPENAI_API_KEY'
```

#### Python

```Python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.list()
```

#### Response

```json
{
    "object": "list",
    "data": [
        {
            "object": "fine-tune",
            "id": "ft-XXXXX",
            "hyperparams": {
                "n_epochs": 4,
                "batch_size": 1,
                "prompt_loss_weight": 0.01,
                "learning_rate_multiplier": 0.1
            },
            "organization_id": "org-XXXXX",
            "model": "ada",
            "training_files": [
                {
                    "object": "file",
                    "id": "file-XXXXX",
                    "purpose": "fine-tune",
                    "filename": "data/prepared_train.jsonl",
                    "bytes": 60800,
                    "created_at": 1678202345,
                    "status": "processed",
                    "status_details": null
                }
            ],
            "validation_files": [],
            "result_files": [],
            "created_at": 1678202346,
            "updated_at": 1678229499,
            "status": "cancelled",
            "fine_tuned_model": null
        }
    ]
}
```

### 단일 Fine-Tune Job 조회

#### HTTP API

```shell
curl https://api.openai.com/v1/fine-tunes/{fine_tune_id} \
  -H "Authorization: Bearer OPENAI_API_KEY"
```

#### Python

```Python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.retrieve(
    id="fine_tune_id"
)
```

| Parameter        | 설명                       |
|------------------|--------------------------|
| `{fine_tune_id}` | 조회를 원하는 Fine-Tune Job ID |

#### Response

```json
{
    "object": "fine-tune",
    "id": "ft-XXXXX",
    "hyperparams": {
        "n_epochs": 4,
        "batch_size": 1,
        "prompt_loss_weight": 0.01,
        "learning_rate_multiplier": 0.1
    },
    "organization_id": "org-XXXXX",
    "model": "ada",
    "training_files": [
        {
            "object": "file",
            "id": "file-XXXXX",
            "purpose": "fine-tune",
            "filename": "data/prepared_train.jsonl",
            "bytes": 60800,
            "created_at": 1678202345,
            "status": "processed",
            "status_details": null
        }
    ],
    "validation_files": [],
    "result_files": [],
    "created_at": 1678202346,
    "updated_at": 1678229499,
    "status": "cancelled",
    "fine_tuned_model": null
}
```

### 단일 Fine-Tune Model Event 조회

#### HTTP API

```shell
curl https://api.openai.com/v1/fine-tunes/{fine_tune_id}/events \
  -H "Authorization: Bearer OPENAI_API_KEY"
```

#### Python

```Python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTune.stream_events(
    id="fine_tune_id"
)
```

| Parameter        | 설명                       |
|------------------|--------------------------|
| `{fine_tune_id}` | 조회를 원하는 Fine-Tune Job ID |

#### Response

```json
[
    {
        "created_at": 1678266902,
        "level": "info",
        "message": "Created fine-tune: ft-XXXXX",
        "object": "fine-tune-event"
    }
    {
        "created_at": 1678267042,
        "level": "info",
        "message": "Fine-tune cancelled",
        "object": "fine-tune-event"
    }
]
```

### 삭제

#### HTTP API

```shell
curl https://api.openai.com/v1/models/{model} \
  -X DELETE \
  -H "Authorization: Bearer OPENAI_API_KEY"
```

#### Python

```Python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.delete(
    sid="{}:{}".format("model_name", "model_id")
)
```

| Parameters   | 설명                                                                    |
|--------------|-----------------------------------------------------------------------|
| `MODEL_NAME` | Fine-Tune 을 생성할 때 지정해준 원본 Model 이름. <br> ada, babbage, curie, davinci |
| `MODEL_ID`   | 생성된 Fine-Tune ID                                                      |
| `{model}`    | `{MODEL_NAME}:{MODEL_ID}` 형식으로 입력합니다.                                 |

#### Response

```json

```