# OpenAI

## 소개

### [OpenAI](https://openai.com/)

> The OpenAI API can be applied to virtually any task that involves understanding or generating natural language or
> code.
> We offer a spectrum of models with different levels of power suitable for different tasks,
> as well as the ability to fine-tune your own custom models.
> These models can be used for everything from content generation to semantic search and
> classification. - [OpenAI Documentation](https://platform.openai.com/docs/introduction)

**OpenAI** 는 **자연어 또는 코드를 이해**하고 이를 이용해 **생성하는 것과 관련된 모든 작업**을 수행하는데 특화된 AI 입니다.

이를 위해 OpenAI 에서는 아래와 같은 기능을 제공합니다.

* [다양한 모델](https://platform.openai.com/docs/models)
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

> [공식 Docs - 모델 소개](https://platform.openai.com/docs/models)

### Turbo

> ChatGPT 에서 사용하는 모델.

* 대화식 채팅 입력 및 출력에 최적화되어 있습니다.
* 특화
    * **대화와 텍스트 생성**

### Davinci

> 가장 뛰어난 모델, 대신 비싸고 느림.

* 다른 모델에 비해 가장 좋은 성능을 가지고 있습니다.
* 다른 모델이 수행할 수 있는 모든 작업을 수행할 수 있으며, 종종 더 적은 량의 대화로 기능이 수행될 수 있습니다.
* 특정 청중을 위한 요약 및 창의적인 콘텐츠 생성같은 많은 이해가 필요한 응용 프로그램의 경우 최상의 결과를 생성합니다.
* 텍스트의 의도를 이해하여 논리 문제를 해결하고 등장 인물의 동기를 설명하는데 뛰어납니다.
* 대신, 더 많은 컴퓨팅 리소스가 필요하므로 다른 모델에 비해 API 호출 당 비용이 많이 들고, 속도도 느립니다.
* 특화
    * **복잡한 의도, 원인과 결과, 청중을 위한 요약**

### Curie

> Q&A 서비스 챗봇 특화 모델.

* 수행 속도가 매우 빠르다고 소개됩니다.
* 감정 분류 및 요약과 같은 미묘한 작업 (nuanced tasks) 을 수행하는데 특화되어 있습니다.
* 질문에 답하는 Q&A 서비스 챗봇으로 가장 적합한 모델입니다.
* 특화
    * **언어 번역, 복잡한 분류, 텍스트 감성, 요약**

### Babbage

> 간단한 분류 특화 모델.

* 간단한 분류와 같은 간단한 작업을 수행하는데 특화되어 있습니다.
* 대표적으로 해당 문서가 검색 쿼리와 얼마나 잘 일치하는지 순위를 매기는 시맨틱 검색에 가장 적절한 모델입니다.
* 특화
    * **보통 분류, 시맨틱 검색**

> 시맨틱 검색이란?
>
> Semantic search denotes search with meaning, as distinguished from lexical search where the search engine looks for
> literal matches of the query words or variants of them, without understanding the overall meaning of the
> query. - [위키피디아](https://en.wikipedia.org/wiki/Semantic_search)

### Ada

> 간단한 주소 수정, 텍스트 파싱 특화 모델. 가장 빠릅니다.

* 다른 모델에 비해 가장 빠른 모델입니다.
* 텍스트 구문 분석, 주소 수정 및 많은 뉘앙스가 필요하지 않은 특정 종류의 분류 작업을 수행하는데 특화되어 있습니다.
* 더 많은 컨텍스트를 제공함으로써 성능이 향상될 수 있습니다.
* Ada 가 제공하는 기능들은 모두 Curie, Davinci 가 수행할 수 있습니다.
* 특화
    * **텍스트 파싱 (Parsing), 단순 분류, 주소 수정, 키워드**

### Codex

> 프로그래밍 코드 생성 특화 모델.

* 프로그래밍 코드 생성 및 수정에 특화되어 있는 모델입니다.
* Python 에 가장 강하며 그 외에도 Javascript, Go, Perl, PHP, Ruby, Swift, Typescript, SQL, Shell 등 12 개 이상의 언어를 사용할 수 있습니다.
* 현재 제한된 베터 기간을 진행 중이며, 이 기간 동안에는 무료로 사용할 수 있으나 속도 제한이 걸려 있습니다.
* 이 기간 동안 [Google 의 사용 정책](https://platform.openai.com/docs/usage-policies)을 준수하는 어플리케이션은 Codex 모델을 사용할 수 있습니다.
* 현재 (2023 년 3 월) 두 가지 Codex 모델을 제공합니다.

| Model            | Description                               | Max Request       | Training Data |
|------------------|-------------------------------------------|-------------------|---------------|
| code-davinci-002 | 자연어를 코드로 바꾸거나 기존의 코드에 기능을 추가하는 기능을 제공합니다. | 8000 tokens       | Jun 2021      |
| code-cushman-001 | 위 모델보다 속도는 빠르지만 유능하진 않습니다.                | Up to 2048 tokens |               |

### DALL·E

> 자연어 To 이미지 특화 모델.

* 사용자가 입력한 자연어를 이용해 이미지를 만들어내는데 특화되어 있습니다.
* 자연어에서 새로운 이미지를 생성하거나 기존 이미지를 편집할 수 있습니다.
* 또한, 사용자가 제공한 이미지를 변형하여 다른 이미지로 만들 수 있습니다.
* [Labs Interface](https://labs.openai.com/) 또는 [API](https://platform.openai.com/docs/guides/images/introduction) 를 통해
  사용할 수 있습니다.
* 상용 서비스 중 비슷한
  모델은 [NovelAI](https://novelai.net/), [Midjourney](https://discord.com/invite/midjourney), [Dream by WOMBO](https://dream.ai/create)
  등이 있습니다.

### Whisper

> 음성 To 텍스트 특화 모델.

* 음성 번역 및 언어 식별, 다국어 음성 인식을 수행할 수 있는 멀티태스킹 모델입니다.
* 전체 코드가 [오픈 소스](https://github.com/openai/whisper)로 공개되어 있으며, 오픈 소스 코드와 동일한 버전을 사용하는 모델입니다.
* OpenAI 에서는 다른 방법을 통해 실행하는 것보다 자신의 API 를 통해 실행하는 것이 훨씬 빠르다고 소개합니다.
* 상용 서비스 중 비슷한 모델은 [CLOVA Speech](https://clova.ai/speech) 이 있습니다.

### Moderation

> 검토 가이트 검증 모델.

* OpenAI 를 사용하는 어플리케이션이 [OpenAI 사용 정책](https://platform.openai.com/docs/usage-policies/)을 준수하는지 확인하는
  모델입니다.
* 무엇을 기준으로 확인하는지는 [검토 가이드](https://platform.openai.com/docs/guides/moderation/overview)에서 확인할 수 있습니다.
* 현재 두 가지 Moderation 모델을 제공합니다.

| Model                  | Description                                  |
|------------------------|----------------------------------------------|
| text-moderation-latest | 가장 유능한 검증 모델입니다. 정확도는 stable 모델보다 약간 더 높습니다. |
| text-moderation-stable | latest 모델과 거의 비슷하지만 약간 더 오래되었습니다.            |

## 가격

> [가격 정보](https://openai.com/pricing)

* 2023 년 3 월 기준 가격입니다. 당연한 말이지만 OpenAI 의 정책에 따라 가격은 변동될 수 있습니다.
* 처음엔 초기 지출 한도 또는 할당량이 부여되며 실적을 쌓으면 시간이 지남에 따라 한도가 증가합니다.
    * 할당량 증가에 대한 요청은 [해당 사이트](https://platform.openai.com/forms/quota-increase)에서 진행 가능합니다.
* 처음 가입하면 3 개월간 사용할 수 있는 **$ 5** 무료 크래딧을 줍니다.
* 사용한 만큼 지불이 됩니다.

### Chat

| Model   | Chat    | InstuctGPT | Fine Tuning - Training | Fine Tuning - Usage | Embedding |
|---------|---------|------------|------------------------|---------------------|-----------|
| Turbo   | $ 0.002 | -          | -                      | -                   | -         |
| Davinci | -       | $ 0.0200   | $ 0.0300               | $ 0.1200            | -         |
| Curcie  | -       | $ 0.0020   | $ 0.0030               | $ 0.0120            | -         |
| Babbage | -       | $ 0.0005   | $ 0.0006               | $ 0.0024            | -         |
| Ada     | -       | $ 0.0004   | $ 0.0004               | $ 0.0016            | $0.0004   |

### Image - DALL·E

| Model  | 1024x1024 | 512x512 | 256x256 |
|--------|-----------|---------|---------|
| DALL·E | $ 0.020   | $ 0.018 | $ 0.016 |

### Audio - Whisper

| Model   | Usage              |
|---------|--------------------|
| Whisper | $ 0.006 / 1 minute |