import json
from googletrans import Translator


class GoogleTranslate:
    translator = Translator()

    @classmethod
    def convert_en_to_mn(self, json_filename: str):
        with open(json_filename, 'r') as f:
            data = json.load(f)

        for srt_object in data:
            self.translate(srt_object['content'])
            input()

    @classmethod
    def translate(self, text: str):
        a = self.translator.translate(text, dest='mn', src='en')
        print(a.text)
