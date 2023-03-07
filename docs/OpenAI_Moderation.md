# Moderation - 검증

## 소개

Moderation Endpoint 는 해당 컨텐츠가 [OpenAI 의 사용 정책](https://platform.openai.com/docs/usage-policies/usage-policies)을 준수하는지
확인하는데 사용되는 도구입니다.
기본적으로 해당 요청은 무료입니다.

개발자는 이 기능을 이용하여 요청하는 데이터가 위의 정책을 준수하는지 확인하는 기능을 구현해야 합니다.
만약, 이를 무시하고 정책을 위반하는 요청이 지속되면 어플리케이션의 변경 요구 이후, 계정의 일시 정지 또는 중지를 포함한 추가 조치가 진행될 수 있습니다.

### 지침

> OpenAI 는 해당 기능의 정확성을 늘리기 위해 지속적인 투자와 노력을 하고 있으며,
> 특히 `hate`, `self-harm`, `violence/graphic` 컨텐츠는 더 많은 노력을 기울이고 있습니다.
> 다만, 현재 영어 이외의 언어는 지원하고 있지 않습니다.

| 카테고리             | 설명                                                                      |
|------------------|-------------------------------------------------------------------------|
| hate             | 인종, 성별, 민족, 종교, 국적, 성적 취향, 카스트 제도나 독재자, 정치인을 대상으로 증오 표현, 선동 혹은 조장하는 컨텐츠 |
| hate/threatning  | 특정 그룹에 대한 폭력 또는 심각한 위해를 포함하는 증오 컨텐츠                                     |
| self-harm        | 자살, 절단, 섭식 장애 등 자해 행위를 조장, 장려 또는 묘사하는 컨텐츠                               |
| sexual           | 성적 흥분을 유발하더나 성적 서비스를 촉진하기 위한 컨텐츠 ( 성교육 및 웰빙 제외 )                        |
| sexual/minors    | 18 세 미만의 미성년자를 대상으로하는 성적 컨텐츠                                            |
| violence         | 폭력을 조장하거나 미화하거나 다른 사람의 고통이나 굴욕을 기념하는 컨텐츠                                |
| violence/graphic | 죽음, 폭력 또는 심각한 신체적 상해를 묘사하는 컨텐츠                                          |

### 모델

| Model                    | 2023 년 3 월 기준         | 설명                                           |
|--------------------------|-----------------------|----------------------------------------------|
| `text-moderation-latest` | `text-moderation-004` | 가장 유능한 검증 모델입니다. 정확도는 stable 모델보다 약간 더 높습니다. |
| `text-moderation-stable` | `text-moderation-001` | latest 모델과 거의 비슷하지만 약간 더 오래되었습니다.            |

## 사용법

### HTTP API

```shell
curl https://api.openai.com/v1/moderations \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer OPENAI_API_KEY' \
  -d '{"input": "I want to kill them."}'
```

### Python

```python
import os
import openai

ai_key = os.getenv("OPENAI_API_KEY")

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Moderation.create(
    model="text-moderation-latest",
    input="I want to kill them."
)

print(response)
```

| Parameter | Type                                               | Value      |
|-----------|----------------------------------------------------|------------|
| `model`   | `text-moderation-latest`, `text-moderation-stable` | 검증에 사용한 모델 |
| `input`   | `String`, `List<String>`                           | 검증을 원하는 값  |

### 결과

```json
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
                "hate": 0.18252533674240112,
                "hate/threatening": 0.0032941880635917187,
                "self-harm": 1.9077321944394043e-09,
                "sexual": 9.69763732427964e-07,
                "sexual/minors": 1.3826513267645169e-08,
                "violence": 0.8871539235115051,
                "violence/graphic": 3.196241493697016e-08
            },
            "flagged": true
        }
    ]
}
```

| Key               | Type                             | Description                    |
|-------------------|----------------------------------|--------------------------------|
| `id`              | `String`                         | 현재 요청의 ID                      |
| `model`           | `String`                         | 실제로 사용된 Model 이름               |
| `results`         | `List<Result>`                   | 사용자의 요청에 대한 결과값                |
| `flagged`         | `Boolean`                        | 사용자의 요청에 대한 OpenAI 사용 정책 위반 여부 |
| `categories`      | `Map<Category, Boolean>`         | 각 검증 카테고리별 결과 값                |
| `category_scores` | `Map<Category, Double( 0 ~ 1 )>` | 각 검증 카테고리별 원시 점수 값             |
