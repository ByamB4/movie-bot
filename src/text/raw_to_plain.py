from configs import DEBUG_LEVEL
from text.srt_to_json import SrtToJson


class RawToPlain:
    def __init__(self, srt_filename: str, out_filename: str):
        if DEBUG_LEVEL == 2:
            print(f'[*] Converting: {srt_filename} to {out_filename}')
        SrtToJson.convert(srt_filename, out_filename)
