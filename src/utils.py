import wave


def get_audio_length(filepath):
    wf = wave.open(filepath, 'rb')
    return wf.getnframes() / wf.getframerate()
