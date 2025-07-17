# 🧠 PromSense Model

**PromSense Model**은 한국어 사용자로부터 입력된 문장을  
고도화된 영어 이미지 생성 프롬프트로 변환하기 위한 AI 백엔드 모델 프로젝트입니다.

이 저장소는 PromSense 웹 서비스와 연동될 모델을 구성하고 있으며,  
**카나나(Kanana) 데이터셋 기반으로 파인튜닝된 SLLM 모델**과  
**LangChain 기반의 RAG 구조**, 그리고 **LoRA**를 활용한 경량화 학습을 포함합니다.

---

## 🚀 프로젝트 개요

- 한국어 프롬프트 → 영어 이미지 생성 프롬프트 자동화
- **Kanana 데이터셋** 기반의 SLLM 모델 학습
- LangChain + RAG 구조로 추론 정확도 보완
- LoRA 방식으로 학습 비용 최소화
- 프론트엔드([promsense](https://github.com/Seorins/promsense))와 연동되는 백엔드 역할

---

## 🛠 기술 스택

| 구분       | 내용 |
|------------|------|
| 언어        | Python 3.x |
| 모델 구조   | SLLM (Kanana 기반 fine-tuning) |
| 최적화 방식 | LoRA |
| 프롬프트 생성 | LangChain + RAG |
| 기타        | Jupyter Notebooks, Docker |
