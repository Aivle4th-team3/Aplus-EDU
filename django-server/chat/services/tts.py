from gtts import gTTS
import io
import base64


# TTS: Text-to-Speech
# gTTS 라이브러리를 사용
def tts(text):
    tts = gTTS(text, lang="ko")

    # 음성을 메모리에 저장하지 않고 Base64로 변환
    speech_data = io.BytesIO()
    tts.write_to_fp(speech_data)
    speech_data.seek(0)  # 파일 끝을 처음으로 돌립니다.

    # Base64로 변환
    base64_encoded = base64.b64encode(speech_data.read()).decode("utf-8")

    return base64_encoded
