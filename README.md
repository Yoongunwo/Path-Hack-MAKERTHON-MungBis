# Path-Hack-MAKERTHON-MungBis

## ABOUT
- 이 프로젝트는 PATH-HACK-MAKERTHON에서 무박 2일동안 만든 작품입니다.
- 강아지가 짖는 정도에 따라 다르게 반응하는 인공지능 음성 인식 기반의 Smart Toy
- 이 작품을 창작하게 된 계기는 강아지 혼자 있는 집안에 개 짖는 소리로 인한 소음 발생 문제를 방지하고자 만든 작품입니다.
- 자세한 동작 원리(`Main/main.py`)는 코드`main.py`를 보면 알 수 있다.

## 동작 원리
1. PATH-HACK-MAKERTHON의 후원사인 ZAM's Lab에서 발명한 인공지능 음성인식 모듈을 통해서 동작이 이루어졌다.
2. 인공지능 음성인식 모듈에 "WalWal" "MungMung"을 학습시킨다.
3. 라즈베리 파이와 프로그램을 실행시킬 컴퓨터가 같은 와이파이를 사용하도록 설정한다.
4. 학습시킨 단어에 해당하는 음성인식이 들어올 경우 해당 모듈은 OutPut으로 "WalWal" 또는 "MungMung"을
  유선으로 라즈베리파이에 값으로 넘긴 후 무선 통신으로 컴퓨터에 값을 넘긴다.
5. 이 값을 받으면 해당 작품은 랜덤으로 상,하,좌,우 중 3방향으로 순차적으로 이동 하면서\
  3색 LED를 동작한다.
6. 4번 동작을 반복한다.


## VERSION
- 개발 보드 : Raspberry Pi 4 Model B
- 컴파일러 : Visual Studio
- 버전 : Python 3.9.2
        Raspberry Pi Imager 1.7.3
        
## MODULE
- 인공지능 음성인식 모듈
- 릴레이 모듈 4개
- DC 모터 2개
- 3색 LED

## 이미지
![toy](https://user-images.githubusercontent.com/97718735/221469904-e8e8112d-6d0e-4c1d-9f41-dbc607718d8f.png)

## 동작영상
- [영상 링크](https://youtube.com/shorts/a16QkHUnHBI)

## Team 
- 기획자 : 심현지
- 메이커 : 김해찬, 양호열
- 개발자 : 윤건우
- 디자이너 : 김구하

## LICENSE
Code released under the [MIT](https://github.com/StartBootstrap/startbootstrap-clean-blog-jekyll/blob/master/LICENSE) license.
