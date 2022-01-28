# 프로젝트 Descroption

에이블러를 위한 스터디 게시판 구현

&nbsp;
### 환경 설치

채팅 사용을 위한 설치

```
docker run -p 6379:6379 -d redis:5(도커의 redis를 사용함)

python -m pip install -U channels

python -m pip install channels_redis
```

다른 포트 연결

```
redis 서버를 다시만들고 config 부분에 CHANNEL_LAYERS 부분 구성을 다시해줌
```

## 프로젝트 정보

windows 환경에서 VSCode를 사용하여 개발

&nbsp;
### 개발 환경 및 사용 기술

개발 언어

```
Python,HTML,CSS,JavaScript
```
framework
```
Django
```

Django Channel을 이용하여 웹소켓 연동
```
도커에 redis port를 구성하여 Django와 연동하여 웹소켓을 사용함
```

## 프로젝트 결과물

기능 및 결과 예시 화면
&nbsp;

### 로그인, 회원가입 구현
- Django 내 authentication 기능 사용 

- 로그인
![login](https://user-images.githubusercontent.com/94459523/151492540-8ceece9c-0b7f-4db7-99d6-f86ebd4d15e1.PNG)

- 회원가입
![캡처](https://user-images.githubusercontent.com/94459523/151493346-b8d99a30-c0e9-4e3d-b969-07a4bdb07f47.PNG)

### 실시간 채팅 구현
- 채팅 
![채팅](https://user-images.githubusercontent.com/76045608/151493872-3ecc6b9a-1dd8-44d2-87d4-9b825788a0de.PNG)

### Q&A 및 자유게시판 구현
```
https://user-images.githubusercontent.com/85106442/151490754-d84556d5-2707-42f1-82c6-91a81bd6b29b.png
```
### Ranking 시스템
- 각 사용자들의 Score를 기반으로 랭킹
![랭크](https://user-images.githubusercontent.com/96154446/151490568-d780c1b8-793f-4342-8f96-175f9d3d97d8.PNG)

### 학습 
- AIVLE 수업 때 수강했던 모든 강의 및 PDF 다운 지원
![aivle 강의](https://user-images.githubusercontent.com/96154446/151490651-b039e1c6-eadd-4266-b576-c1f0236a687d.PNG)

### 퀴즈 구현
- 퀴즈 메인
![퀴즈1](https://user-images.githubusercontent.com/76045608/151493840-73024c4f-7ebd-4eaf-8f1a-bc502e6c4537.PNG)
- 퀴즈 저장
![퀴즈2](https://user-images.githubusercontent.com/76045608/151493862-93caa8a8-e549-4063-88fb-f907a1915538.PNG)

### 유튜브 강의장 구현
- 개발 입문에 도움되는 유명한 유튜브 자료
- 카드 형식으로 제작 
![유튜브강의장](https://user-images.githubusercontent.com/94459523/151494271-97d9c35b-10e6-4778-ae16-41012c9d2a51.PNG)

