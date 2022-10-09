import os
from selenium.webdriver.chrome.options import Options

DEBUG_LEVEL = 1
PROJECT_NAME = os.path.dirname(os.path.abspath(__file__)).split('/')[-2]


def get_driver_options():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-bookmarks")
    options.add_argument("--incognito")
    options.add_argument("--start-fullscreen")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disk-cache-size=0")
    options.add_argument("--disk-cache-dir=/dev/null")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("headless")
    options.add_argument("mute-audio")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    return options


def get_project_root():
    cwd = os.path.dirname(os.path.abspath(__file__))
    return cwd[:cwd.find(PROJECT_NAME) + len(PROJECT_NAME)]


STATIC_ROOT = os.path.join(get_project_root(), 'static')

# User controlled
SOURCE_SRT = f'{STATIC_ROOT}/source/sub.srt'
SOURCE_VIDEO = f'{STATIC_ROOT}/source/video.mp4'

# Runtime files
DEST_PROCESSED_SRT = f'{STATIC_ROOT}/dest/processed-srt.json'
DEST_SENTENCES = f'{STATIC_ROOT}/dest/sentences.json'
DEST_TRANSLATED = f'{STATIC_ROOT}/dest/mn-translated.json'
DEST_AUDIO_ROOT = f'{STATIC_ROOT}/dest/audio'
DEST_VIDEO_ROOT = f'{STATIC_ROOT}/dest/video'
