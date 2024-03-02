# tts, stt 모두 활용
# 인공지능 스피커와 대화

import time, os

# 음성 인식을 위한 
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# 음성인식 (듣기) - stt
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = 'ko')
        print('[김규식] ' + text)
        answer(text) 
    except sr.UnknownValueError:
        print("음성인식 실패") 
    except sr.RequestError: 
        print("요청 실패! : {0}" .format(e)) # API key 오류, 네트워크 단절 등..


# 스피커가 할 대답 정해주는 함수
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = "안녕하세요. 반갑습니다!"
    elif '날씨' in input_text:
        answer_text = "오늘 서울의 기온은 5도 입니다. 맑은 하늘이 예상됩니다."
    elif '환율' in input_text:
        answer_text = "1달러 환율은 1380원 입니다."
    elif '고마워' in input_text:
        answer_text = "별 말씀을요. 제 일인걸요."
    elif '종료' in input_text:
        answer_text = "네 다음에 또 만나요!"
        stop_listening(wait_for_stop = False)
    elif '김경식' in input_text:
        answer_text = "김경식은 머리는 좋지만 말 안듣고 고집은 엄청난 이 집의 둘째 아들입니다. 서울대에 다니지만 혼자서 손톱도 못 깍는 사람이지요."
    else:
        answer_text = "잘 이해하지 못했어요."
    speak(answer_text)


# 소리내어 읽기(tts)
def speak(text):
    print('[인공지능] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text = text, lang = 'ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)


# 객체들 
r = sr.Recognizer() # 마이크로부터 음성을 인식 받을 수 있게 하는 객체
m = sr.Microphone() # 마이크로부터 들려오는 음성

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen) # 종료하지 않고 계속 듣고 있을 수 있게
# stop_listening(wait_for_stop = False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)