from translate.google_translate import GoogleTranslate
from text.raw_to_plain import RawToPlain
from configs import get_static_root

# RawToPlain(f'{get_static_root()}/demo.srt', f'{get_static_root()}/out.json')
GoogleTranslate.convert_en_to_mn(f'{get_static_root()}/out.json')
