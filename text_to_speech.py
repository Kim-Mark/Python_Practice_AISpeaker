# TTS(Text to speech) - 글자를 음성으로 ex. 키오스크, 전자 음성
# STT(Speech to text) - 음성을 글자로

# 가상환경 설치 - python -m venv myenv     /myenv: 이름
# 가상환경 활성화 - .\myenv\Scripts\activate
# 패키지 설치 - pip install gTTS / pip install playsound==1.2.2

from gtts import gTTS # 구글에서 제공하는 tts 기능

# play sound 이용 - 파일이 저장됨과 동시에 소스코드 내에서 바로 소리 재생
from playsound import playsound

# text 음성 저장할 파일 이름 설정
file_name = 'sample.mp3' 

# 영어 문장
#text = "Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight."
#tts_en = gTTS(text=text, lang = 'en') # 말하고자 하는 text를 영어로 인식해서 음성으로 바꾼 결과
#tts_en.save(file_name)


# 한글문장
#text = "저는 기계입니다. 하지만 쓸 만한 놈이에요"
#tts_ko = gTTS(text = text, lang = 'ko')
#tts_ko.save(file_name)
#playsound(file_name)

# 긴 문장 - 파일에서 텍스트를 불러와서 처리하도록
with open('sample.txt', "r", encoding = 'utf8') as f:  # sample.txt 파일을 읽기모드로 열어서 불러오기
    text = f.read()
tts_ko = gTTS(text = text, lang = 'ko')
tts_ko.save(file_name) # 저장
playsound(file_name)

