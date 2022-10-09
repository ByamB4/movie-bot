from translate import GoogleTranslate
from text import SrtToJson, JsonToTranslationText
from voice import Chimege, FixAudio
from video import VideoCreation


def job() -> None:
    SrtToJson()
    JsonToTranslationText()
    GoogleTranslate()
    Chimege()
    FixAudio()
    VideoCreation()


if __name__ == '__main__':
    job()
