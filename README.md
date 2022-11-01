# README

### ✨ 팀 소개

내배캠스프링 B-1조 League of Developer 팀입니다. 게임을 좋아하는 각각의 팀원이 모여 이제 게임보다는 코딩에 집중하자는 목표로 지은 팀명입니다. 다들 잔잔하지만 맡은 일에 최선을 다 합니다.

<BR>

###  🔥 팀 목표

* 게임보다는 코딩에 집중하자!

* 낙오하지 말자!

* 어엿한 개발자가 되자!

<BR>

### 💡 팀 약속

1. 지각, 무단결석 하지 않기

2. 9시, 14시, 17시 스크럼 진행(생존신고, 질문 및 진행상황 공유…)

3. 서로 짜증내지 않고, 배려하고 존중하기

4. 판교에서 만나자! 

<BR>

### 개발 인원 및 역할

5명

김영민 : 팀장 (프론트)

김석진 : 팀원 (백엔드), 조원 페이지 불러오기

성루비 : 팀원 (프론트), 

이승윤 : 팀원 (백엔드), 방명록 작성

최승호 : 팀원 (백엔드), 방명록 불러오기(역할)

<BR>

### 📌 프로젝트 소개

내배캠스프링 B-1팀과 팀원을 소개하는 웹페이지를 제작합니다.

* LOD팀의 정보를 알 수 있다.
* 메인페이지에서 팀 정보를 확인할 수 있다.
* 메인페이지에서 각 팀원 페이지로 이동할 수 있다.
* 팀원 페이지에서 각 팀원의 정보를 알 수 있다.
* 각 팀원 페이지의 방명록을 작성할 수 있다.

<br>

### 📌 사용된 기술

프론트 : HTML, CSS, JS

백엔드 : Flask, Python

DB : MongoDB

<br>

### 📌 데이터베이스 구조

**[member]** - 팀원 정보 테이블

|    field    | value |
| :---------: | :---: |
|     id      |  int  |
|    name     |  str  |
| description |  str  |
|    mbti     |  str  |
|   stpoint   |  str  |
|    style    |  str  |
|    blog     |  str  |

<br>

**[visited]** - 방명록 테이블

|   field   | value |
| :-------: | :---: |
|    id     |  str  |
|  comment  |  str  |
| member_id |  int  |

<br>

### 📌 API

| 기능                 | Method | URL                      | Request                             | Response                                                     |
| -------------------- | ------ | ------------------------ | ----------------------------------- | ------------------------------------------------------------ |
| 조원 페이지 불러오기 | GET    | '/{id}'                  |                                     | {"id": 1, "name": "이름", "mbti": "infp",  "desc": "소개글", "stpoint": "장점", "style": "업무스타일", "blog": "블로그주소",} |
| 방명록 불러오기      | GET    | '/visit/{member_id}'     |                                     | {"id": "닉네임", "comment": "방명록 내용", "member_id": 해당 페이지 팀원 id} |
| 방명록 작성          | POST   | '/visit/add/{member_id}' | 닉네임, 코멘트, 해당 페이지 팀원 id | 작성된 닉네임, 코멘트                                        |
| 뒤로 가기            | GET    | '/home'                  |                                     | 메인페이지                                                   |

<br>

### 📌 프레임워크
![img](https://lh4.googleusercontent.com/E5tFNHA__KQiUS6NVoe3X36JUWq_ZySeBD3aihLwpxm5DxBOse1Ss8TzdKuMkAFXeWjY9zXjmp5ilwU-fwrF2IzHwd4c2WAqVjaJO_5i_0urvJkhloJHUzVJ8s4i9sFLIPqajlxqyCVFD8p_Qr1GCJdzR3NZpVqukbzzQWa-0Hggd368633eBc_-)![img](https://lh6.googleusercontent.com/HKDc0z9jYbtwyq_SDxglGOFcw3vDoyN5FpS1wDoHcx8Z7YqDPrnGcnJ4IeHKlIrvrf15YuD6wIH6QqUEkgnRuteXcj2DiiLcDILV_XIB6Y8oxJ_9riIwTLDklxwgqksIjFObo0aLURI93f4AMV8AXm0fadaavRJrvHs7TiaI_kdlaPtpv4hhvap9)