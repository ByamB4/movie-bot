from translate import GoogleTranslate
from text import SrtToJson, JsonToTranslationText
from voice import Chimege
# from video import UpdateAudioSpeed


def job() -> None:
    SrtToJson()
    JsonToTranslationText()
    GoogleTranslate()
    Chimege()


if __name__ == '__main__':
    job()
