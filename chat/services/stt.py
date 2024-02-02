import base64
import io
import tempfile
import whisper

# STT: Speech-to-Text
# whisper 라이브러리를 사용
def stt(audio_message):

    # 포맷 변환
    audio_data = base64.b64decode(audio_message)
    audio_stream = io.BytesIO(audio_data)

    # 임시 파일에 오디오 데이터를 쓰기
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tmp_file.write(audio_stream.read())
        temp_file_path = tmp_file.name

    # 모델 로드 및 트랜스크립션 수행
    model = whisper.load_model("base")
    transformed = model.transcribe(temp_file_path)
    return transformed['text']
