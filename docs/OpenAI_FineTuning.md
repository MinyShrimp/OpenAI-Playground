# Fine-Tuning - 미세 조정

> 사전 학습 데이터를 기준으로 새로운 프롬프트의 값을 추출하는 기법 - [미세 조정 가이드](https://platform.openai.com/docs/guides/fine-tuning)

OpenAPI 가 제공하는 API 대신 GPT-3 을 사용하여 자신의 어플리케이션에 맞게 모델을 미세 조정하는 기능입니다.
GTP-3.5 출시 이전에 사용되던 GPT-3 을 사용하기 때문에 사전에 개방형 인터넷에서 훈련된 모델에
사용자가 원하는 데이터를 입력하여 자신의 어플리케이션에 특화된 데이터를 얻어낼 수 있게 됩니다.

미세 조정을 위해서는 다음 단계를 진행해야 합니다.

* 학습 데이터 준비 및 업로드
* 미세 조정된 새 모델 학습
* 미세 조정된 모델 사용

미세 조정이 완료된 모델은 프롬프트에 예제를 제공하지 않아도 답을 얻을 수 있으며,
이로 인해 기존의 API 를 사용하는 것보다 절감된 비용과 빠른 응답 속도를 얻을 수 있습니다.