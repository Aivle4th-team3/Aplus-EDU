# AI 교육 플랫폼 A+EDU

> AI를 학생으로 활용하여 자기주도 학습하는 교육 서비스

**주관** : [KT](https://aivle.kt.co.kr/home/main/indexMain)　　　　　**소속** : KT 에이블스쿨 4기 수도권 1반 3조　　　　　**프로젝트 기간** : 2023-12-11 ~ 2024-01-12

## 🚩 목차

-   [📖 프로젝트 소개](#-프로젝트-소개)
-   [🧑‍💻 팀 소개](#-팀-소개)
-   [🎥 데모](#-데모)
-   [💡 주요 기능](#-주요-기능)
-   [🎨 UI](#-ui)
-   [🛠️ 기술 스택](#%EF%B8%8F-기술-스택)
-   [⚙️ 구현 세부 사항](#%EF%B8%8F-구현-세부-사항)
-   [📝 기술 블로그](https://aivle4-team3.github.io/Aplus-EDU)
-   [🏗️ ERD](#%EF%B8%8F-erd)
-   [📂 프로젝트 구조](#-프로젝트-구조)
-   [🚀 실행 방법](#-실행-방법)

## 📖 프로젝트 소개

<table>
  <tr>
    <td>
      &nbsp;&nbsp;&nbsp;미국의 응용행동과학연구에서는 외부 정보가 인간의 뇌에 저장되는 방법을 기준으로 가장 효과적인 학습 방법을 피라미드 계층으로 정리하여 제안하였습니다.<br> 
      &nbsp;&nbsp;&nbsp;학습 피라미드에 따르면 학습한 내용을 직접 설명하고 가르치는 방식이 가장 효율적임을 알 수 있습니다.<br> 
      &nbsp;&nbsp;&nbsp;A+EDU는 능동적 학습 방법과 생성형 AI 기술을 결합한 자기주도 학습 서비스를 제공하여, 성취도 평가와 피드백을 통해 학습 과정의 부족한 부분을 보완하고 오개념 학습을 예방하는 교육 플랫폼입니다.
    </td>
    <td style="text-align: right;" width="350" height="300">
      <img alt="learnig-pyramid" src="https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/4b73b36a-bbd3-468e-9dda-4fb68a041b8e"  width="350" height="250">
    </td>
  </tr>
</table>

## 🧑‍💻 팀 소개

|                                     [김영진](https://github.com/yxxngjxn)                                      |                                    [김진우](https://github.com/MooYaHo1)                                    |                                     [안진수](https://github.com/Awlstn)                                     |                                    [유승호](https://github.com/pumple99)                                     |                                       [임형섭](https://github.com/h3lim)                                        |                                   [정원철](https://github.com/NarciSource)                                    |
| :------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
| ![Youngjean](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/e5faed59-eea1-4329-bd6e-2e9eacb816de) | ![Jinwoo](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/6250e602-e081-4c14-83b2-4d7637b32464) | ![Jinsoo](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/5372d886-1a51-445b-9144-bf822f9f67c8) | ![Seungho](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/2e013e61-e41d-4003-8014-3e1b373cceb8) | ![Hyeongseop](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/0cea3bbc-636d-470c-953d-8b1df30ebbde) | ![Woncheol](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/71771b95-2a4e-4eac-a236-452b6f7ee919) |

## 🎥 데모

https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/95064514-1fbb-4706-8cf7-e42de7d532d7

## 💡 주요 기능

1.  웹 페이지

    -   사용자 회원가입, 로그인 관리
    -   OAuth로 Github, Google, Naver, Kakao 계정 연동
    -   게시판, 댓글 작성
    -   ckeditor로 편집 가능한 게시글 작성
    -   내 게시글에 댓글 달림시 알람
    -   사용자 일정 관리

2.  동영상 강의

    -   강의 등록
    -   강의 당 여러편의 동영상 등록
    -   강의 시청 및 평가

3.  학생AI와 채팅

    -   채팅방을 통해 학생 AI와 채팅
    -   채팅을 통한 학생AI 학습 (벡터데이터베이스)
    -   음성 입력으로 채팅 (STT)
    -   학생AI의 응답을 음성화 (TTS)

4.  평가
    -   저장된 평가지에 맞춰 학생AI의 평가
    -   문항 당 점수와 해설
    -   전체 문항 점수를 고려한 등급 평가

## 🎨 UI

<img alt="첫 페이지창" src="https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/9c7b9701-a77e-4ff0-a2ec-55b36d5f4b9d" style="width:49%;"> <img alt="로그인창" src="https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/5a3f721f-d0ec-42e2-8c36-3005b318707a" style="width:49%;"> <img alt="강의 목록창" src="https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/7f220aa8-0977-49bb-995b-0314419ea78b" style="width:49%;"> <img alt="채팅창" src="https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/23ef0b19-6647-42d8-9fc8-4f143b6959be" style="width:49%;"> <img alt="평가창" src="https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/aead9216-aa7b-47ac-9515-7cc0eb5a2535" style="width:49%;">

## 🛠️ 기술 스택

### AI

[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=LangChain&logoColor=white)](https://www.langchain.com) [![OpenAI](https://img.shields.io/badge/OpenAI-%23412991?style=flat-square&logo=openai&logoColor=white)](https://platform.openai.com) [![Gemini](https://img.shields.io/badge/Gemini-%238E75B2?style=flat-square&logo=googlegemini&logoColor=white)](https://ai.google.dev) [![LLaMA](https://img.shields.io/badge/LLaMA-%230467DF?style=flat-square&logo=meta)](https://llama.meta.com/llama3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-351C75?style=flat-square)](https://huggingface.co) [![Ollama](https://img.shields.io/badge/Ollama-whitesmoke.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMTgxLjAwMDAwMHB0IiBoZWlnaHQ9IjI1Ni4wMDAwMDBwdCIgdmlld0JveD0iMCAwIDE4MS4wMDAwMDAgMjU2LjAwMDAwMCIKIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiPgoKPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsMjU2LjAwMDAwMCkgc2NhbGUoMC4xMDAwMDAsLTAuMTAwMDAwKSIKZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSJub25lIj4KPHBhdGggZD0iTTM3NyAyMzY1IGMtNTIgLTE4IC04MyAtNDkgLTExNyAtMTE2IC00NSAtODkgLTYyIC0xOTIgLTU4IC0zNTUgbDMKLTE0MiAtNTggLTYxIGMtMTQ4IC0xNTUgLTE4NSAtMzg3IC05MiAtNTc0IGwzNCAtNjkgLTIwIC00NCBjLTM0IC04MiAtNTAKLTE2NCAtNTAgLTI2MyAwIC0xMDggMTggLTE5MCA1OCAtMjYyIGwyNiAtNDggLTIxIC00OSBjLTEyIC0yNyAtMjYgLTcxIC0zMgotOTggLTE0IC02MiAtMTUgLTIyMSAtMSAtMjU3IDEwIC0yNiAxNCAtMjcgNzYgLTI3IDczIDAgNzAgLTQgNTMgODYgLTE1IDgyIDIKMTg4IDQyIDI2NiAzNyA3MCAzOCAxMDQgNSAxNDggLTQ3IDY0IC02OCAxMzYgLTY5IDI0MCAtMSAxMDMgMTQgMTYwIDY2IDI2MQozMSA2MSAyOSA4NyAtMTAgMTIyIC0xMSAxMCAtMzEgNDIgLTQzIDcwIC0xOSA0MiAtMjQgNjkgLTIzIDE0MiAwIDExNCAyNSAxODMKOTUgMjYwIDcwIDc2IDE0MiAxMTAgMjM5IDExMiA0MSAwIDc4IDIgODIgMiA0IDEgMTcgMjIgMjkgNDcgMzAgNTkgOTYgMTE5CjE2NyAxNTIgNDkgMjMgNzAgMjcgMTQ3IDI3IDc5IDAgOTcgLTQgMTQ5IC0yOSA2OCAtMzMgMTMzIC05NCAxNTkgLTE0OCAxMAotMjAgMjMgLTQxIDMwIC00NSA2IC00IDQ2IC04IDg3IC04IDY3IC0xIDgzIC01IDE0MCAtMzYgMTIzIC02OCAxOTMgLTE4NyAxOTMKLTMzNCAxIC02NyAtNCAtOTAgLTI3IC0xNDIgLTE2IC0zNSAtMzUgLTY4IC00MyAtNzUgLTM0IC0yOCAtMzUgLTU4IC01IC0xMTcKNTIgLTEwMSA2NyAtMTU4IDY2IC0yNjEgLTEgLTEwNCAtMjIgLTE3NiAtNjkgLTI0MCAtMzMgLTQ0IC0zMiAtNzggNSAtMTQ4IDQwCi03OCA1NyAtMTg0IDQyIC0yNjYgLTE3IC05MCAtMjAgLTg2IDUzIC04NiA2MiAwIDY2IDEgNzYgMjcgMTQgMzYgMTMgMTk1IC0xCjI1NyAtNiAyNyAtMjAgNzEgLTMyIDk4IGwtMjEgNDkgMjYgNDggYzc2IDEzOSA3OSAzNTkgNiA1MjggbC0yMCA0NyAyNSA0NgpjOTkgMTgzIDY0IDQzOSAtODEgNTkxIGwtNTggNjEgMyAxNDIgYzQgMTY0IC0xMyAyNjYgLTU4IDM1NyAtNjQgMTI2IC0xNzIKMTU5IC0yNjMgNzkgLTU0IC00NyAtOTIgLTEzOCAtMTIzIC0yOTggLTMgLTE0IC0xMCAtMjIgLTE3IC0xOCAtMTgyIDgwIC0yOTcKODUgLTQ0MyAyMSBsLTU0IC0yNCAtNCAyMiBjLTM2IDE4NSAtODUgMjg1IC0xNTYgMzIyIC00MyAyMSAtNzQgMjQgLTExMyAxMHoKbTc3IC0xNjggYzQyIC03MSA4MSAtMzAxIDU3IC0zMzYgLTUgLTggLTMxIC0xNiAtNTggLTE4IC0yNiAtMiAtNjIgLTggLTgwCi0xMyBsLTMxIC04IC03IDQ5IGMtOCA1OSAyIDE3MiAyMiAyNDggMTQgNTcgNDggMTIxIDYzIDEyMSA1IDAgMjAgLTE5IDM0IC00M3oKbTk2NSAxMCBjNDAgLTY1IDY5IC0yMzkgNTYgLTMzNiBsLTcgLTQ5IC0zMSA4IGMtMTggNSAtNTQgMTEgLTgwIDEzIC0yNyAyCi01MyAxMCAtNTggMTggLTEyIDE3IC0zIDE0MSAxNyAyMjkgMTUgNjQgNTcgMTUwIDc0IDE1MCA0IDAgMTggLTE1IDI5IC0zM3oiLz4KPHBhdGggZD0iTTc3OCAxMzYxIGMtNzMgLTI0IC0xMTYgLTUxIC0xNjUgLTEwNCAtNTUgLTYwIC03NiAtMTIwIC03MSAtMjAxIDUKLTc2IDM1IC0xMjkgMTA2IC0xODMgNjIgLTQ3IDEyNyAtNjMgMjU3IC02MyAxNzIgMCAyNTggMzYgMzI5IDEzOCA0MiA1OSA0OAoxNTUgMTYgMjMwIC0yOSA2OCAtMTExIDE0MyAtMTg4IDE3MyAtODAgMzEgLTIwNyAzNiAtMjg0IDEweiBtMjU3IC0xMDAgYzE2MQotNzEgMTk0IC0yMzIgNjYgLTMxOCAtNDkgLTMzIC05NCAtNDMgLTE5NiAtNDMgLTEwMiAwIC0xNDcgMTAgLTE5NiA0MyAtMTc4CjEyMCAtMzIgMzU2IDIxMSAzNDMgMzkgLTIgODYgLTEyIDExNSAtMjV6Ii8+CjxwYXRoIGQ9Ik04MzggMTE1OSBjLTI1IC0xNCAtMjIgLTQ0IDcgLTY3IDIwIC0xNiAyNCAtMjYgMTkgLTQ5IC03IC0zNiAxNQotNTggNTEgLTQ5IDIxIDUgMjUgMTIgMjUgNDYgMCAyOSA1IDQyIDIwIDUwIDI3IDE1IDI3IDY2IDAgNzUgLTEwIDMgLTI4IDEKLTQwIC01IC0xNCAtNyAtMjYgLTggLTM5IDAgLTIzIDEyIC0yMiAxMiAtNDMgLTF6Ii8+CjxwYXRoIGQ9Ik0zOTcgMTM0OCBjLTkgLTcgLTIzIC0zMCAtMzIgLTUwIC0yMSAtNTMgLTEgLTEwMyA0NyAtMTE2IDQzIC0xMSA2MAotNiA5MiAyNyA0MCA0MSA0MyA4MSAxMSAxMTkgLTIxIDI1IC0zNCAzMiAtNjQgMzIgLTIwIDAgLTQ1IC02IC01NCAtMTJ6Ii8+CjxwYXRoIGQ9Ik0xMjk1IDEzMjggYy0zMiAtMzggLTI5IC03OCAxMSAtMTE5IDMyIC0zMyA0OSAtMzggOTIgLTI3IDQ5IDEzIDY4CjYyIDQ2IDExOCAtMTkgNDcgLTM4IDYwIC04NyA2MCAtMjcgMCAtNDEgLTcgLTYyIC0zMnoiLz4KPC9nPgo8L3N2Zz4K&style=flat-square&logoColor)](https://ollama.com)

### Back-end

[![Django](https://img.shields.io/badge/Django-%23092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/) [![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833?style=flat-square&logo=anaconda&logoColor=white)](https://www.anaconda.com) [![Python](https://img.shields.io/badge/Python-%233776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)

### Front-end

[![Vue.js](https://img.shields.io/badge/Vue.js-%234FC08D?style=flat-square&logo=vuedotjs&logoColor=white)](https://vuejs.org/) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![HTML5](https://img.shields.io/badge/HTML5-%23E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-%231572B6?style=flat-square&logo=css3&logoColor=white)

### Database

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%234169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org) [![Chroma](https://img.shields.io/badge/Chroma-FF6446.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMjU2cHgiIGhlaWdodD0iMTY0cHgiIHZpZXdCb3g9IjAgMCAyNTYgMTY0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiICBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCI+CiAgICA8dGl0bGU+Q2hyb21hPC90aXRsZT4KICAgIDxnPgogICAgICAgIDxlbGxpcHNlIGZpbGw9IiNGRkRFMkQiIGN4PSIxNzAuNjY2Nzk1IiBjeT0iODEuOTE5ODM2MiIgcng9Ijg1LjMzMzIwNTMiIHJ5PSI4MS45MTk4MzYyIj48L2VsbGlwc2U+CiAgICAgICAgPGVsbGlwc2UgZmlsbD0iIzMyN0VGRiIgY3g9Ijg1LjMzMzIwNTMiIGN5PSI4MS45MTk4MzYyIiByeD0iODUuMzMzMjA1MyIgcnk9IjgxLjkxOTgzNjIiPjwvZWxsaXBzZT4KICAgICAgICA8cGF0aCBkPSJNMTcwLjY2Njc5NSw4MS45MTk5NjQyIEMxNzAuNjY2Nzk1LDEyNy4xNjMzOTQgMTMyLjQ2MTQzMSwxNjMuODM5MTYgODUuMzMzMDc3MywxNjMuODM5MTYgTDg1LjMzMzA3NzMsODEuOTE5OTY0MiBMMTcwLjY2Njc5NSw4MS45MTk5NjQyIFogTTg1LjMzMzIwNTMsODEuOTE5ODM2MiBDODUuMzMzMjA1MywzNi42NzY3OTA2IDEyMy41MzgxODUsOC45NTk5ODIwOWUtMDUgMTcwLjY2Njc5NSw4Ljk1OTk4MjA5ZS0wNSBMMTcwLjY2Njc5NSw4MS45MTk4MzYyIEw4NS4zMzMyMDUzLDgxLjkxOTgzNjIgWiIgZmlsbD0iI0ZGNjQ0NiI+PC9wYXRoPgogICAgPC9nPgo8L3N2Zz4K&style=flat-square)](https://www.trychroma.com) [![FAISS](https://img.shields.io/badge/FAISS-%230467DF?style=flat-square&logo=meta)](https://ai.meta.com/tools/faiss) [![Pinecone](https://img.shields.io/badge/Pinecone-black.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMTA2LjAwMDAwMHB0IiBoZWlnaHQ9IjExOS4wMDAwMDBwdCIgdmlld0JveD0iMCAwIDEwNi4wMDAwMDAgMTE5LjAwMDAwMCIKIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiPgoKPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsMTE5LjAwMDAwMCkgc2NhbGUoMC4xMDAwMDAsLTAuMTAwMDAwKSIKZmlsbD0iI0ZGRkZGRiIgc3Ryb2tlPSJub25lIj4KPHBhdGggZD0iTTU1MyAxMTQyIGMtNDUgLTI2IC04NCAtNTAgLTg4IC01MyAtNiAtNyAxNSAtNTkgMjQgLTU5IDMgMCAyNiAxMgo1MCAyNSAyNCAxNCA0NiAyMyA0OSAyMCAzIC0yIDAgLTMwIC03IC02MSAtMTUgLTc3IC0xNiAtNzQgMjMgLTc0IDM0IDAgMzQgMQo0MSA1MyAxMSA4MSAxNyA4NCA1NiAzMyBsMzUgLTQ1IDI3IDIyIDI3IDIyIC00NiA1NSBjLTc5IDk2IC05MiAxMTAgLTEwMSAxMTAKLTQgMCAtNDUgLTIyIC05MCAtNDh6Ii8+CjxwYXRoIGQ9Ik0yMzAgMTAwOCBjLTIxIC04IC0yNCAtMTcgLTQ0IC0xMzAgLTEzIC03NSAtMTIgLTc3IDggLTgyIDM5IC0xMSA0NQotNiA1MiA0MiAzIDI2IDkgNTEgMTEgNTUgMyA1IDI0IC0xMyA0NyAtMzkgbDQyIC00NyAyNyAxOCAyNyAxNyAtMzEgMzkgYy0xNwoyMSAtMzUgNDEgLTQwIDQ0IC0yMSAxMyAtNyAyNSAzMCAyNSA1NyAwIDcxIDggNzEgNDIgbDAgMzAgLTkxIC00IGMtNDkgLTIKLTk5IC02IC0xMDkgLTEweiIvPgo8cGF0aCBkPSJNNzg3IDk0MSBjLTMgLTkgLTggLTIzIC0xMSAtMzIgLTYgLTEzIDQgLTIxIDQzIC0zNSAyOCAtMTAgNTEgLTIxCjUxIC0yNiAwIC00IC0yNCAtMjAgLTUyIC0zNCAtMjkgLTE1IC01NCAtMjggLTU2IC0yOSAtMSAtMSA1IC0xNiAxNCAtMzIgbDE3Ci0yOSA1NCAyOSBjMzAgMTYgNTYgMjcgNTkgMjQgMyAtMyAxIC0yOCAtNCAtNTYgLTggLTQ2IC03IC01MSA5IC01MSA5IDAgMjQKLTMgMzIgLTYgMTEgLTQgMTggMTYgMzIgOTIgMTIgNjUgMTQgMTAzIDggMTEzIC01IDggLTUxIDMyIC0xMDAgNTIgLTc5IDMyCi05MiAzNSAtOTYgMjB6Ii8+CjxwYXRoIGQ9Ik00NzggNzc4IGwtODYgLTUxIDE2IC0yNiBjOSAtMTQgMTcgLTI4IDE4IC0yOSAxIC0yIDIzIDggNDkgMjMgMjUKMTUgNDggMjUgNTEgMjMgMiAtMyAtMSAtMjggLTcgLTU3IC0xMyAtNjIgLTggLTgxIDI1IC04MSAyNyAwIDMzIDEwIDQyIDgwIDQKMjcgOSA1MCAxMSA1MCAzIDAgMjIgLTE5IDQzIC00MiAzOCAtNDMgMzggLTQzIDU5IC0yNCAxMiAxMSAyMSAyMiAyMSAyNiAwIDE0Ci0xMzEgMTYwIC0xNDMgMTYwIC03IC0xIC01MSAtMjQgLTk5IC01MnoiLz4KPHBhdGggZD0iTTg1IDY5OCBjLTM5IC0zMyAtNzQgLTY3IC03OCAtNzUgLTUgLTkgOCAtNDQgMzkgLTEwMSAyNiAtNDggNDggLTg4CjQ5IC05MCA1IC02IDU1IDIyIDU1IDMwIDAgNSAtOSAyNyAtMjEgNDkgLTExIDIzIC0xOCA0MyAtMTUgNDYgMyAzIDMwIDEgNjAKLTQgMzEgLTYgNTggLTggNjEgLTUgMyAzIDUgMTggNSAzMyAwIDI0IC00IDI4IC00MiAzNCAtODUgMTMgLTg1IDEzIC0zOSA1OQpsNDEgNDIgLTIyIDIyIC0yMyAyMSAtNzAgLTYxeiIvPgo8cGF0aCBkPSJNOTI4IDYwMiBsLTI3IC0xOCAyNCAtNDMgYzE0IC0yNCAyNSAtNDYgMjUgLTUxIDAgLTQgLTE5IC00IC00MiAxCi03NSAxNCAtODUgMTIgLTkwIC0yMSAtNSAtMzEgLTggLTMwIDg1IC00NiBsMzkgLTcgLTQxIC00MSBjLTQwIC00MSAtNDAgLTQxCi0yMiAtNjUgMTkgLTI0IDE5IC0yNCA0MyAtNSA4NiA2OCAxMjggMTExIDEyOCAxMzAgMCAxNyAtODUgMTg0IC05MyAxODQgLTEgMAotMTQgLTggLTI5IC0xOHoiLz4KPHBhdGggZD0iTTQyMiA0NDUgYy00MSAtMjQgLTc2IC00NiAtODAgLTQ5IC03IC04IDE5IC01NiAzMCAtNTYgNSAwIDI3IDEyIDQ5CjI2IDIzIDE0IDQzIDIzIDQ2IDIwIDMgLTIgMCAtMjggLTYgLTU2IC0xNiAtNzIgLTE0IC03NyAxOSAtODIgMzMgLTUgMzUgLTEKNDUgNjggNCAyNyAxMCA1MyAxMiA1NyAzIDQgMjEgLTEyIDQxIC0zNyBsMzYgLTQ0IDI3IDIwIDI4IDIxIC02NiA3OCBjLTQ1IDU0Ci03MyA3OSAtODcgNzggLTEyIDAgLTU0IC0yMCAtOTQgLTQ0eiIvPgo8cGF0aCBkPSJNOTYgMzQ4IGMtNyAtNDEgLTEwIC0xNjcgLTQgLTE3MyAzIC0zIDQ4IC0xOCAxMDEgLTM0IDYzIC0xOSA5NyAtMjUKOTcgLTE4IDAgNyAzIDIyIDYgMzMgNSAxOSAtMSAyMyAtNDUgMzUgLTI4IDcgLTUxIDE2IC01MSAyMCAwIDQgMjMgMjEgNTAgMzkKMjggMTggNTAgMzQgNTAgMzcgMCAzIC04IDE2IC0xOSAyOSBsLTE4IDIzIC00OSAtMzQgYy0yNyAtMTkgLTUyIC0zNSAtNTUgLTM1Ci0zIDAgLTQgMjUgLTEgNTUgbDQgNTUgLTMwIDAgYy0yNiAwIC0zMSAtNCAtMzYgLTMyeiIvPgo8cGF0aCBkPSJNNjkxIDI0MSBsLTI1IC0xOSAzMiAtNDkgYzE4IC0yNyAzMiAtNTMgMzIgLTU4IDAgLTQgLTI1IC01IC01NSAtMQpsLTU1IDYgMCAtMzMgMCAtMzQgOTggLTYgYzU4IC0zIDEwMSAtMiAxMDcgNCAxNCAxNCA2NCAxODMgNTYgMTkxIC0zIDMgLTE3IDgKLTMxIDEwIC0yMSAzIC0yNiAtMyAtMzggLTQ0IC03IC0yNyAtMTcgLTQ4IC0yMiAtNDggLTQgMCAtMjIgMjMgLTQwIDUwIC0xOAoyOCAtMzMgNTAgLTM0IDUwIDAgMCAtMTIgLTkgLTI1IC0xOXoiLz4KPHBhdGggZD0iTTQwNSAxMTUgYy00NCAtNDQgLTIxIC0xMDUgNDAgLTEwNSA0MyAwIDY1IDIyIDY1IDY1IDAgNjEgLTYxIDg0Ci0xMDUgNDB6Ii8+CjwvZz4KPC9zdmc+Cg==&style=flat-square&logoColor=white)](https://www.pinecone.io) [![SQLite](https://img.shields.io/badge/SQLite-%23003B57?style=flat-square&logo=sqlite)](https://www.sqlite.org/)

### IaaS

[![AWS](https://img.shields.io/badge/AWS-%23232F3E?style=flat-square&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ko) [![AWS S3](https://img.shields.io/badge/Amazon%20S3-%23569A31?style=flat-square&logo=amazons3&logoColor=white)](https://aws.amazon.com/ko/s3) [![GoogleDrive](https://img.shields.io/badge/GoogleDrive-%234285F4?style=flat-square&logo=googledrive&logoColor=white)](https://developers.google.com/drive/api)

## ⚙️ 구현 세부 사항

-   Django을 이용하여 웹어플리케이션 구현
-   Django ORM을 이용하여 PostgreSQL 데이터베이스를 제어
-   ASGI로 웹소켓 채팅
-   Vue.js를 이용하여 인터렉티브한 SPA
-   Prompt Engineering으로 LLM이 특정 작업을 수행하도록 지시하여 응답을 유도
-   LangChain 프레임워크를 통해 템플릿, LLM과 벡터 데이터베이스의 파이프라인을 구축
-   LLM으로 GPT, Gemini, LLaMA 또는 HuggingFace 등 다양한 모델의 API을 유연하게 전환 가능
-   Ollama를 사용해 로컬에서 LLM 모델 실행도 가능
-   Vector Database를 사용한 컨텍스트 관리로 LLM의 기억 저장소 역할 - Chroma, FAISS, Pinecone
-   AWS에서 EC2와 S3를 사용하여 웹 호스팅

## [📝 기술 블로그](https://Aivle4th-team3.github.io/Aplus-EDU)

## 🏗️ ERD

![ERD](https://github.com/Aivle4th-team3/Aplus-EDU/assets/26417221/d74ca32c-6e4d-488b-a381-d710bc4e66c8)

## 📂 프로젝트 구조

<details>
<summary>열기</summary>

```
Aplus-EDU
├─ .git
├─ .gitattributes
├─ .gitignore
├─ .gitmodules
├─ accounts
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ signals.py
│  ├─ urls.py
│  ├─ urls_allauth.py
│  ├─ views.py
│  └─ __init__.py
├─ board
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ signals.py
│  ├─ templatetags
│  │  └─ url_utils.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ chat
│  ├─ admin.py
│  ├─ apps.py
│  ├─ asgi.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_remove_message_bot_message_embedded_and_more.py
│  │  ├─ 0003_remove_message_user_remove_message_video_and_more.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ services
│  │  ├─ stt.py
│  │  └─ tts.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ websocket
│  │  ├─ consumers.py
│  │  └─ urls.py
│  └─ __init__.py
├─ config
│  ├─ asgi.py
│  ├─ asset_storage.py
│  ├─ message.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ core
│  └─ templatetags
│     ├─ form_tags.py
│     ├─ markdown_tags.py
│     └─ svg_tags.py
├─ dist
│  └─ student_ai-0.3.8-py3-none-any.whl
├─ evaluation
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_remove_testresult_testpaper_testresult_message.py
│  │  ├─ 0003_remove_testresult_message_testresult_testpaper_and_more.py
│  │  ├─ 0004_rename_scrore_testresult_score_and_more.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ home
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ lecture
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_alter_lecture_thumbnail_alter_video_file.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ README.md
├─ requirements.txt
├─ static
│  ├─ accounts
│  │  ├─ css
│  │  │  ├─ avatar.css
│  │  │  ├─ consent.css
│  │  │  ├─ signup.css
│  │  │  └─ social-btn.css
│  │  ├─ img
│  │  │  ├─ babyRobot.png
│  │  │  └─ Rei.jpg
│  │  ├─ js
│  │  │  ├─ enableAgree.js
│  │  │  └─ read-image.js
│  │  └─ md
│  │     ├─ personal_agreement.md
│  │     └─ terms_of_use.md
│  ├─ board
│  │  ├─ css
│  │  │  ├─ post_detail.css
│  │  │  └─ post_form.css
│  │  └─ js
│  │     ├─ popupDelete.js
│  │     └─ postsInjection.js
│  ├─ chat
│  │  ├─ css
│  │  │  ├─ app-chat.css
│  │  │  ├─ loading.css
│  │  │  └─ record-voice.css
│  │  ├─ img
│  │  │  ├─ gpt_logo.svg
│  │  │  └─ loading.svg
│  │  └─ js
│  │     ├─ chat.js
│  │     ├─ loading.js
│  │     └─ recordVoice.js
│  ├─ common
│  │  ├─ img
│  │  │  └─ system.png
│  │  └─ lifeQuotes.txt
│  ├─ evaluation
│  │  ├─ img
│  │  │  ├─ A.png
│  │  │  ├─ B.png
│  │  │  ├─ C.png
│  │  │  ├─ D.png
│  │  │  └─ F.png
│  │  └─ js
│  │     ├─ eachEvalsChartBuilder.js
│  │     ├─ historyChartBuilder.js
│  │     ├─ personalChartBuilder.js
│  │     └─ todayEvalsChartBuilder.js
│  ├─ frontdoor
│  │  ├─ css
│  │  │  ├─ avatar.css
│  │  │  ├─ background.css
│  │  │  ├─ footer.css
│  │  │  └─ happynewyear.css
│  │  ├─ img
│  │  │  ├─ babyRobot__1.png
│  │  │  ├─ babyRobot__2.png
│  │  │  ├─ babyRobot__3.png
│  │  │  ├─ babyRobot__4.png
│  │  │  ├─ babyRobot__5.png
│  │  │  ├─ banner (1).png
│  │  │  ├─ banner (2).png
│  │  │  ├─ banner (3).png
│  │  │  ├─ blank profile.png
│  │  │  ├─ EDU.png
│  │  │  ├─ Hyeongseop.png
│  │  │  ├─ Jinsoo.png
│  │  │  ├─ Jinwoo.png
│  │  │  ├─ logoText.png
│  │  │  ├─ profile.png
│  │  │  ├─ robot.gif
│  │  │  ├─ robot1.png
│  │  │  ├─ robot2.png
│  │  │  ├─ robot3.png
│  │  │  ├─ robot4.png
│  │  │  ├─ robot5.png
│  │  │  ├─ Seungho.png
│  │  │  ├─ Woncheol.png
│  │  │  └─ Yeongjin.png
│  │  └─ js
│  │     ├─ frontdoor.js
│  │     └─ happynewyear.js
│  ├─ home
│  │  ├─ css
│  │  │  ├─ faq.css
│  │  │  ├─ home.css
│  │  │  ├─ main.css
│  │  │  └─ snow.css
│  │  ├─ js
│  │  │  ├─ main.js
│  │  │  ├─ readComment.js
│  │  │  ├─ slidePhrase.js
│  │  │  └─ snow.js
│  │  └─ md
│  │     └─ faq.md
│  ├─ lecture
│  │  ├─ css
│  │  │  └─ modal.css
│  │  ├─ img
│  │  │  └─ converse_with_ai.png
│  │  └─ js
│  │     ├─ modal.js
│  │     └─ videoInjection.js
│  └─ vendor
│     ├─ css
│     │  ├─ bootstrap.css
│     │  ├─ sb-admin-2.min.css
│     │  └─ three-dots.css
│     ├─ js
│     │  ├─ bootstrap.js
│     │  └─ menu.js
│     └─ sneat-bootstrap
│        ├─ app-academy.css
│        ├─ app-calendar-events.js
│        ├─ app-calendar.css
│        ├─ app-calendar.js
│        ├─ config.js
│        ├─ core.css
│        ├─ helpers.js
│        └─ theme-default.css
├─ templates
│  ├─ account
│  │  ├─ avatar.html
│  │  ├─ consent.html
│  │  ├─ login.html
│  │  ├─ mypage.html
│  │  ├─ password_reset.html
│  │  ├─ signup.html
│  │  └─ socialbuttons.html
│  ├─ board
│  │  ├─ confirm_delete.html
│  │  ├─ post_detail.html
│  │  └─ post_form.html
│  ├─ chat
│  │  ├─ loading.html
│  │  └─ page.html
│  ├─ evaluation
│  │  ├─ page.html
│  │  └─ personal.html
│  ├─ frontdoor
│  │  ├─ base.html
│  │  ├─ happynewyear.html
│  │  ├─ index.html
│  │  ├─ introduction.html
│  │  └─ topbar.html
│  ├─ home
│  │  ├─ base.html
│  │  ├─ faq.html
│  │  ├─ layout.html
│  │  ├─ main.html
│  │  ├─ sidebar.html
│  │  └─ topbar.html
│  ├─ lecture
│  │  ├─ room.html
│  │  └─ showcase.html
│  └─ socialaccount
│     └─ signup.html
└─ _student-ai

```

</details>

## 🚀 실행 방법

1.  요구 패키지 설치  
    `pip install -r requirements.txt`
2.  환경 변수 입력 .env 파일을 루트 폴더 아래에 생성

```Python
ENVIRONMENT= # DEVELOPE (로컬) | PRODUCTION (AWS)
DJANGO_SECRET_KEY= # https://django-secret-key-generator.netlify.app 에서 발급

GITHUB_OAUTH_CLIENT_ID= # https://github.com/settings/developers 새 앱 만들고 Client ID
GITHUB_OAUTH_SECRET= # ...Client secrets
GOOGLE_OAUTH_CLIENT_ID= # https://console.cloud.google.com/apis/credentials 사용자 인증 정보 만들고 클라이언트 ID
GOOGLE_OAUTH_SECRET= # ...클라이언트 보안 비밀번호
NAVER_OAUTH_CLIENT_ID= # https://developers.naver.com/apps 애플리케이션 등록 - 네이버 로그인 API 등록하고 Client ID
NAVER_OAUTH_SECRET= # ...Client Secret
KAKAO_OAUTH_CLIENT_ID= # https://developers.kakao.com/console/app 애플리케이션 추가하기 - 앱 키 - REST API 키
KAKAO_OAUTH_SECRET # ...보안 - Client Secret

DB_MASTER_USER_ID= # 데이터베이스 유저 아이디
DB_MASTER_USER_PWD= # 데이터베이스 유저 비밀번호
DB_HOST= # (로컬) http://localhost | (AWS): https://console.aws.amazon.com/rds - Endpoint

AWS_ACCESS_KEY_ID= # https://aws.amazon.com/ko/iam - 엑세스 키 ID
AWS_SECRET_ACCESS_KEY= # ...비밀 엑세스 키

LLM_PROVIDER= # OPENAI | GOOGLE | HUGGINGFACEHUB | OLLAMA
EMBEDDING_PROVIDER= # OPENAI | GOOGLE | HUGGINGFACEHUB
VECTORSTORE_PROVIDER= # Chroma | FAISS | PINECONE

OPENAI_API_KEY= # https://platform.openai.com/settings/profile?tab=api-keys
GOOGLE_API_KEY= # https://aistudio.google.com/app/apikey
HUGGINGFACEHUB_API_TOKEN= # https://huggingface.co/settings/tokens

OPENAI_LLM_MODEL= # gpt-3.5-turbo | gpt-4 | gpt-4-turbo
GOOGLE_LLM_MODEL= # text-bison@001 | text-bison@002 | gemini-pro
HUGGINGFACEHUB_LLM_MODEL= # mistralai/Mistral-7B-Instruct-v0.2 | https://huggingface.co/models?other=LLM
OLLAMA_LLM_MODEL= # llama3 | phi3 | wizardlm2 | https://ollama.com/library

GOOGLE_EMBEDDING_MODEL= # models/embedding-001
HUGGINGFACEHUB_EMBEDDING_MODEL= # jhgan/ko-sroberta-nli | https://huggingface.co/models?other=embeddings
```

3. 데이터베이스로 장고ORM 마이그레이션  
   `python manage.py migrate`
4. 장고 서버 실행  
   `python manage.py runserver`
5. 관리자 계정 생성  
   `python manage.py createsuperuser`
