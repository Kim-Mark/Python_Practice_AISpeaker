# 음성을 인식해서 문자로 리턴
# 패키지 설치 - (음성인식 모듈)pip install SpeechRecognition / (마이크 사용 모듈) pip install PyAudio
import speech_recognition as sr 
r = sr.Recognizer() # 마이크로 부터 인식 받게 할 수 있게

# 파일로부터 음성 불러오기 (wav, aiff, flac)
#r = sr.recongizer()
#with sr.AudioFile("파일명") as source:
#    print("듣고 있어요.")
#    audio = r.record(source)


# 마이크로부터 들려오는 음성 저장
with sr.Microphone() as source:
    print("듣고 있어요")
    audio = r.listen(source) # 마이크로부터 음성 듣기

# audio에 저장된 음성을 텍스트로 변환 / 예외처리까지(인터넷 연결, 음성의 질...)
# 구글 내에 있는 모듈을 사용 - 녹음된 데이터를 구글 서버로 전달하면 서버에서 작업 후 텍스트로 리턴

try:
    # 구글 API 사용 - 하루 50회 사용 가능

    # 영어
    #text = r.recognize_google(audio, language = 'en-US') # 저장된 음성, 음성의 언어 / text로 변환
    #print(text)

    # 한국어
    text = r.recognize_google(audio, language = "ko-KO")
    print(text)

except sr.UnknownValueError:
    print("음성인식 실패") 
except sr.RequestError: 
    print("요청 실패! : {0}" .format(e)) # API key 오류, 네트워크 단절 등..