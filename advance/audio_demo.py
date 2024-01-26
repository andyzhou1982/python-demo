import wave
import pyaudio

def play_wav_stream(wav_file):
    # 打开WAV流文件
    wav_stream = wave.open(wav_file, 'rb')
    # 初始化音频流
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=audio.get_format_from_width(wav_stream.getsampwidth()),
        channels=wav_stream.getnchannels(),
        rate=wav_stream.getframerate(),
        output=True
    )
    # 播放音频流
    chunk_size = 1024
    data = wav_stream.readframes(chunk_size)
    while data:
        stream.write(data)
        data = wav_stream.readframes(chunk_size)
    # 关闭音频流和文件
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wav_stream.close()

# 播放WAV流文件
stream_file = 'resources/output.tmp.wav'
play_wav_stream(stream_file)

