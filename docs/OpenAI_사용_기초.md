# OpenAI 사용 - 기초

## OPENAI_API_KEY 발급

> [View API Keys](https://platform.openai.com/account/api-keys) ( 로그인 필요 )

## HTTP API

### 모델 목록 확인

```sh
curl https://api.openai.com/v1/models \
  -H 'Authorization: Bearer OPENAI_API_KEY'
```

### Completions 보내기

```sh
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer OPENAI_API_KEY" \
  -d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
```

## Python

```sh
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

### Python CLI

```sh
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

```sh
$ openai api completions.create \
    -m text-davinci-003 -p "Say this is a test" \
    -t 0 -M 7 --stream
```

## NodeJS

```sh
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
