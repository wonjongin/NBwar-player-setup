# NBwar Player Setup

NBwar 사용을 위한 모드들을 자동으로 설치해 주는 프로그램 입니다.
 
기존의 모드들은 삭제되니 주의해 주시기 바랍니다.

## 설치 방법

[다운로드](https://github.com/wonjongin/NBwar-player-setup/releases) 에서 자신의 OS 에 맞는 파일을 다운 받아 주십시오.
(만약 자신의 OS가 없다면 [직접 실행하기](#직접-실행하기)를 읽어주십시오)

다운로드가 다 되었으면 더블클릭으로 실행하십시오 

실행 하셨다면 시작하기 버튼을 눌러 주십시오.

마지막에 "완료되었습니다. 종료를 눌러주십시오" 라는 메시지가 나오면 성공하신 것 입니다.

## 주의사항

* 기존의 모드들이 삭제 됩니다. 백업등의 작업을 해주시기 바랍니다.
* 프로그램이 처음 켜질 때 느릴 수 있습니다. 양해 부탁드립니다.
* 프로그램이 실행되는 동안에는 마인크래프트와 런처는 꼭 꺼 주시기 바랍니다.  

## 직접 실행하기

이 프로그램은 파이썬으로 작성되었습니다. 그래서 직접 실행하기 위해서는 파이썬이 필요하므로 파이썬을 설치해 주시기 바랍니다.

파이썬이 설치되었다면 다음을 입력하시기 바랍니다.

```shell script
git clone https://github.com/wonjongin/NBwar-player-setup.git
cd NBwar-player-setup
pip3 install -r requirements.txt
python3 app.py
```