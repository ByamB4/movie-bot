import re
import json
from sys import argv


class SrtToJson:
    @classmethod
    def convert(self, srt_filename: str, out_filename: str):
        srt = open(srt_filename, 'r', encoding="utf-8").read()
        parsed_srt = self.parse_srt(srt)
        open(out_filename, 'w', encoding="utf-8").write(
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
