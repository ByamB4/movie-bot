from configs import DEBUG_LEVEL, SOURCE_SRT, DEST_PROCESSED_SRT, DEST_SENTENCES
import re
import json


class SrtToJson:
    def __init__(self):
        self.convert()
        if DEBUG_LEVEL == 1:
            print(f'[+] Converted srt to json')

    def convert(self):
        srt = open(SOURCE_SRT, 'r', encoding="utf-8").read()
        parsed_srt = self.parse_srt(srt)
        open(DEST_PROCESSED_SRT, 'w', encoding="utf-8").write(
            json.dumps(parsed_srt, indent=2, sort_keys=True))

    @classmethod
    def parse_time(self, time_string):
        hours = int(re.findall(r'(\d+):\d+:\d+,\d+', time_string)[0])
        minutes = int(re.findall(r'\d+:(\d+):\d+,\d+', time_string)[0])
        seconds = int(re.findall(r'\d+:\d+:(\d+),\d+', time_string)[0])
        milliseconds = int(re.findall(r'\d+:\d+:\d+,(\d+)', time_string)[0])

        return (hours * 3600 + minutes * 60 + seconds) * 1000 + milliseconds

    @classmethod
    def parse_srt(self, srt_string):
        srt_list = []

        for line in srt_string.split('\n\n'):
            if line != '':
                index = int(re.match(r'\d+', line).group())

                pos = re.search(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+',
                                line).end() + 1
                content = line[pos:]
                start_time_string = re.findall(
                    r'(\d+:\d+:\d+,\d+) --> \d+:\d+:\d+,\d+', line)[0]
                end_time_string = re.findall(
                    r'\d+:\d+:\d+,\d+ --> (\d+:\d+:\d+,\d+)', line)[0]
                start_time = self.parse_time(start_time_string)
                end_time = self.parse_time(end_time_string)

                srt_list.append({
                    'index': index,
                    'content': content.replace('\u00a0', '').replace('\n', ' ').replace('\u2019', '\'').replace('\u201d', '\'').replace('\u201c', '\'').replace('\u2018', '\''),
                    'start': start_time,
                    'end': end_time
                })

        return srt_list


class JsonToTranslationText:
    def __init__(self):
        self.to_translation_text()

    def to_translation_text(self):
        # TODO
        # sentences = []

        # with open(DEST_PROCESSED_SRT, 'r') as f:
        #     data = json.load(f)

        # sentences = ''

        # for obj in data:
        #     sentences += obj['content']

        # sentences = sentences.replace('i.e.', '')
        # sentences = sentences.split('.')

        # clean_data = []
        # i, last_index = 0, 0

        # for sentence in sentences:
        #     if sentence == '':
        #         continue

        #     for index in range(last_index, len(data)):
        #         is_there = False

        #         for part in data[index]['content'].split('.'):
        #             if part in sentence:
        #                 is_there = True
        #                 break

        #         if is_there:
        #             clean_data.append({
        #                 'content': sentence,
        #                 'start': data[index]['start'],
        #                 'end': data[last_index]['end'],
        #                 'index': i
        #             })
        #             last_index = index
        #             i += 1
        #             break

        # with open(DEST_SENTENCES, 'w') as f:
        #     json.dump(clean_data, f, ensure_ascii=False, indent=2)

        with open(DEST_PROCESSED_SRT, 'r') as f:
            data = json.load(f)

        with open(DEST_SENTENCES, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        if DEBUG_LEVEL == 1:
            print('[+] Converted to sentences')
