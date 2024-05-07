import wave

def get_wav_content(wav_file='resources/tts_01.wav'):
    with open(wav_file,'rb') as f:
        hex = f.read().hex()
        return hex

def get_wav_info(wav_file='resources/tts_01.wav'):
    wav_info = {}
    with wave.open(wav_file, 'rb') as f:
        wav_info['nchannels'] = f.getnchannels()
        wav_info['sampwidth'] = f.getsampwidth()
        wav_info['framerate'] = f.getframerate()
        wav_info['nframes'] = f.getnframes()
        wav_info['comptype'] = f.getcomptype()
        wav_info['compname'] = f.getcompname()
    return wav_info

if __name__ == '__main__':
    result = get_wav_content()
    print(result)