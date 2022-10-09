from configs import DEST_TRANSLATED, DEST_AUDIO_ROOT
from requests import post
import os
import base64
import json


class Chimege:
    URL: str = 'https://reader.chimege.com/api/v2/demo'

    def __init__(self) -> None:
        self.convert_texts_to_audio()

    def convert_texts_to_audio(self) -> None:
        os.mkdir(DEST_AUDIO_ROOT)
        with open(DEST_TRANSLATED, 'r') as f:
            data = json.load(f)
        print(f'[*] Converting to audios (chimege): {len(data)}')
        for obj in data:
            # print(f'\t[*] Processing: {obj["index"]}')
            data = self.get_voice(self.clean_data(obj['content']))
            decoded = base64.b64decode(data['data'])
            with open(f"{DEST_AUDIO_ROOT}/{obj['index']}-{obj['start']}-{obj['end']}.wav", 'wb') as of:
                of.write(decoded)
            if int(obj['index']) % 50 == 0:
                print(f'\t[*] Processing: {obj["index"]}')

    def get_voice(self, text: str) -> None:
        try:
            data = post(f'{self.URL}?voiceID=2&speed=1',
                        data=text.encode('utf-8'))
            if data.json()['message'] == 'ok':
                return data.json()
        except Exception as e:
            print(f'\t[-] Error: {e}')
            print(f'\t[-] Input data: {text}')
            input()

    # temporary thing
    def clean_data(self, text: str) -> str:
        words = text.split()
        if words[0] == 'ч':
            return ' '.join(words[1:])
        return text
