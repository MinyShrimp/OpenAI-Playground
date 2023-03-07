# OpenAI

## 소개

### [OpenAI](https://openai.com/)

> The OpenAI API can be applied to virtually any task that involves understanding or generating natural language or
> code.
> We offer a spectrum of models with different levels of power suitable for different tasks,
> as well as the ability to fine-tune your own custom models.
> These models can be used for everything from content generation to semantic search and classification.
> ( [OpenAI Documentation](https://platform.openai.com/docs/introduction) )

**OpenAI** 는 **자연어 또는 코드를 이해**하고 이를 이용해 **생성하는 것과 관련된 모든 작업**을 수행하는데 특화된 AI 입니다.

이를 위해 OpenAI 에서는 아래와 같은 기능을 제공합니다.

* [모델](https://platform.openai.com/docs/models)
* [텍스트 완성 - Text Completion](https://platform.openai.com/docs/guides/completion)
* [코드 완성 - Code Completion](https://platform.openai.com/docs/guides/code)
* [채팅 - Chat Completion (ChatGPT)](https://platform.openai.com/docs/guides/chat)
* [이미지 생성 - Image Generation](https://platform.openai.com/docs/guides/images)
* [미세 조정 - Fine Tuning](https://platform.openai.com/docs/guides/fine-tuning)
* [Embedding](https://platform.openai.com/docs/guides/embeddings)
* [음성을 문자로 - Speech to Text](https://platform.openai.com/docs/guides/speech-to-text)
    * 유사한 서비스로는 네이버의 [CLOVA Speech](https://clova.ai/speech)가 있습니다.
* [검증 - Moderation](https://platform.openai.com/docs/guides/moderation/overview)
    * 해당 콘텐츠가 [OpenAI 의 사용 정책](https://platform.openai.com/docs/api-reference/moderations)을 준수하는지 확인합니다.
    * 2023 년 3 월 기준, 영어만 사용 가능 합니다.

이 기능들을 사용해서 **새로운 콘텐츠 생성**은 물론, **의미 검색 및 분류**로 이용할 수 있습니다.

## 모델

## 기능

### fine-tuning

사전 학습 데이터를 기준으로 새로운 프롬프트의 값을 추출하는 기법

### classification

상품명/옵션명을 기준으로 제조사/브랜드. 카테고리가 분류된 데이터를 모델링하여 학습하는 기법

- 새로운 상품명/옵션명이 입력될 때 미리 학습된 데이터 기준으로 제조사/브랜드를 추출하는 방법론에 대한 기술

## 사용

### OPENAI_API_KEY 발급

> [View API Keys](https://platform.openai.com/account/api-keys) ( 로그인 필요 )

### HTTP API

#### 모델 목록 확인

```http
curl https://api.openai.com/v1/models \
  -H 'Authorization: Bearer OPENAI_API_KEY'
```

#### Completions 보내기

```http
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer OPENAI_API_KEY" \
  -d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
```

### Python

```console
$ pip install openai
```

```python
import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Say this is a test",
    temperature=0,
    max_tokens=7
)

print(response)
```

#### Python CLI

```console
$ openai -h
usage: openai [-h] [-v] [-b API_BASE] [-k API_KEY] [-o ORGANIZATION] {api,tools,wandb} ...

positional arguments:
  {api,tools,wandb}
    api                 Direct API calls
    tools               Client side tools for convenience
    wandb               Logging with Weights & Biases

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Set verbosity.
  -b API_BASE, --api-base API_BASE
                        What API base url to use.
  -k API_KEY, --api-key API_KEY
                        What API key to use.
  -o ORGANIZATION, --organization ORGANIZATION
                        Which organization to run as (will use your default organization if not specified)
```

```console
$ openai api completions.create \
    -m text-davinci-003 -p "Say this is a test" \
    -t 0 -M 7 --stream
```

### NodeJS

```console
$ npm install openai
$ yarn install openai
```

```javascript
const {Configuration, OpenAIApi} = require("openai");

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

const response = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: "Say this is a test",
    temperature: 0,
    max_tokens: 7,
});

console.log(response);
```

## OpenAI 를 사용한 오픈 소스 라이브러리

> [전체 목록 확인 하기](https://platform.openai.com/docs/libraries/community-libraries)

### Python

* [chronology](https://github.com/OthersideAI/chronology) by OthersideAI

### Java

* [OpenAI-Java](https://github.com/TheoKanning/openai-java) by TheoKanning

### Kotlin

* [OpenAI-Kotlin](https://github.com/Aallam/openai-kotlin) by Mouaad Aallam

### NodeJS

* [openai-api](https://www.npmjs.com/package/openai-api) by Njerschow
* [openai-api-node](https://www.npmjs.com/package/openai-api-node) by erlapso
* [gpt-x](https://www.npmjs.com/package/gpt-x) by ceifa
* [gpt3](https://www.npmjs.com/package/gpt3) by poteat
* [gpts](https://www.npmjs.com/package/gpts) by thencc
* [@dalenguyen/openai](https://www.npmjs.com/package/@dalenguyen/openai) by dalenguyen
* [tectalic/openai](https://github.com/tectalichq/public-openai-client-js) by tectalic

### C# / .NET

* [OpenAI.GPT3](https://github.com/betalgo/openai) by Betalgo

## 프로젝트 설치

* Python 설치 - [Homepage](https://www.python.org/)
* 프로젝트 복사
    * `git clone https://github.com/MinyShrimp/OpenAI-Playground.git`
    * `cd OpenAI-Playground`
* 가상환경 설정
    * `python -m venv venv`
    * `source venv/bin/activate`
    * `pip install pip --upgrade`
* 라이브러리 설치
    * `pip install -r requirements.txt`
* OpenAI 회원 가입 - [Homepage](https://platform.openai.com/)
* API Key 발급
    * [View API Keys](https://platform.openai.com/account/api-keys) ( 로그인 필요 )
* 환경 설정에 env 등록
    * [common/README.md](/common/README.md) 참고
* 실행
    * `python main.py`