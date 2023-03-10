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

> 훈련 데이터 준비를 위해선 아래의 조건을 만족해야합니다.<br>
> 아래의 글은 간략한 안내만을 진행하기 때문에 더 자세한
> 내용은 [공식 Documentation](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset) 을 참고해주세요.<br>
> 공식 Documentation 에서는 기본적인 조건
> 외에도 [여러 상황에 대한 적절한 솔루션](https://platform.openai.com/docs/guides/fine-tuning/advanced-usage)을 제공합니다.

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

| Parameters     | 설명                                      |
|----------------|-----------------------------------------|
| `<LOCAL_FILE>` | CSV, TSV, XLSX, JSON, JSONL 형식의 Raw 데이터 |

* python 을 통해 openai 를 설치하게 되면 위와 같이 CLI 환경에서 실행할 수 있는 도구를 제공합니다.
* **CSV, TSV, XLSX, JSON, JSONL** 확장자를 지원하며, 결과물은 `<FILENAME>_train.jsonl`과 `<FILENAME>_valid.jsonl` 의 형태로 제공됩니다.
* 위 도구를 실행하면 위에서 말한 필수 조건과 만족하면 좋은 조건이 모두 적용되어 파일이 생성됩니다.

## 훈련 데이터 업로드

> 해당 문서에서는 CLI 도구를 이용한 방법만 소개됩니다.<br>
> 만약 API 를 이용한 방법을 알고 싶다면 [OpenAI_FineTuning_API.md](OpenAI_FineTuning_API.md) 를 참고해주세요.

위의 조건을 만족한 JSONL 파일이 준비되면 해당 파일을 OpenAI 서버에 업로드를 해야합니다.

업로드를 하는 방법은 CLI 도구를 사용하는 방법과 Files API 를 사용하는 방법이 있습니다.

### CLI 업로드 도구

```shell
$ openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
```

| Parameters                | 설명                                                      |
|---------------------------|---------------------------------------------------------|
| `<TRAIN_FILE_ID_OR_PATH>` | `<FILENAME>_train.jsonl` 파일의 경로를 입력합니다.                 |
| `<BASE_MODEL>`            | ada, babbage, curie, davinci 의 모델 중 원하는 모델을 선택해서 입력합니다. |

위의 명령을 실행하면 여러 작업이 수행됩니다.

1. File API 를 사용하여 파일 업로드
2. Fine-Tuning 생성
3. 작업이 완료될 때 까지 이벤트를 스트리밍합니다.
    * 종종 몇 분 정도 걸리지만 대기열에 작업이 많거나 데이터 세트가 큰 경우 몇 시간이 걸릴 수 있습니다.

### 이어서 재 업로드

```shell
$ openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```

| Parameters                | 설명                    |
|---------------------------|-----------------------|
| `<YOUR_FINE_TUNE_JOB_ID>` | 작업을 진행 중인 ID 를 입력합니다. |

만약, 위의 업로드를 진행하다가 여러 이유 (인터넷 접속 불안정, 클라이언트 접속 종료) 로 인해 작업이 중단되면
위의 명령을 실행하여 다시 작업을 이어서 진행할 수 있습니다.

### 현재 진행 상황 확인

```shell
# List all created Fine-Tunes
$ openai api fine_tunes.list

# Retrieve the state of Fine-Tune.
# job status: pending, running, succeeded, failed
$ openai api fine_tunes.get -i <YOUR_FINE_TUNE_JOB_ID>

# Cancel a job
$ openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>
```

| CLI                 | 설명                                                          |
|---------------------|-------------------------------------------------------------|
| `fine_tunes.list`   | 생성된 모든 Fine Tunes 목록을 가져옵니다.                                |
| `fine_tunes.get`    | `<YOUR_FINE_TUNE_JOB_ID>` 을 이용하여 원하는 단일 Fine Tunes 를 가져옵니다. |
| `fine_tunes.cancel` | `fine_tunes.create` 의 진행을 취소합니다.                            |

| Job Status | pending | running | succeeded | failed |
|------------|---------|---------|-----------|--------|
| 설명         | 대기      | 진행 중    | 완료        | 실패     |

## Fine Tuning 모델 사용

> **Completion Endpoint** 를 사용하기 때문에 Completion 이 지원하는 모든 파라미터를 사용할 수 있습니다.<br>
> 이에 대한 자세한 내용은 [공식 Documentation](https://platform.openai.com/docs/api-reference/completions) 에서 확인해주세요.

### CLI

```shell
$ openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
```

| Parameters           | 설명                           |
|----------------------|------------------------------|
| `<FINE_TUNED_MODEL>` | `fine_tunes.create` 로 생성한 모델 |
| `<YOUR_PROMPT>`      | 답변을 원하는 자연어 요청               |

### HTTP API

```shell
curl https://api.openai.com/v1/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "YOUR_PROMPT", "model": "FINE_TUNED_MODEL"}'
```

### Python

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Completion.create(
    model="FINE_TUNED_MODEL",
    prompt="YOUR_PROMPT"
)
```

### NodeJS

```javascript
await openai.createCompletion({
    model: "FINE_TUNED_MODEL"
    prompt: "YOUR_PROMPT",
});
```

## Fine Tuning 모델 삭제

> 해당 모델을 삭제하기 위해서는 해당 모델의 Owner 로 지정되어야 합니다.

### CLI

```shell
$ openai api models.delete -i <FINE_TUNED_MODEL>
```

| Parameters           | 설명                           |
|----------------------|------------------------------|
| `<FINE_TUNED_MODEL>` | `fine_tunes.create` 로 생성한 모델 |

### HTTP API

```shell
curl https://api.openai.com/v1/models/<FINE_TUNED_MODEL> \
  -X "DELETE" \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Python

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.delete(
    model="FINE_TUNED_MODEL"
)
```