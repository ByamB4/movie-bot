import os
from configs import DEST_AUDIO_ROOT, SOURCE_VIDEO, DEST_VIDEO_ROOT
import multiprocessing
from moviepy.editor import (
    AudioFileClip,
    # ImageClip,
    # concatenate_videoclips,
    concatenate_audioclips,
    CompositeAudioClip,
    CompositeVideoClip,
    VideoFileClip
)


class VideoCreation:
    def __init__(self):
        self.combine_audios()

    def combine_audios(self):
        print('Generating final video')
        audios = []
        background_clip = VideoFileClip(SOURCE_VIDEO).without_audio()
        files = [_ for _ in os.listdir(DEST_AUDIO_ROOT)]
        files.sort(key=lambda x: int(x.split('-')[0]))
        for filename in files:
            audios.append(
                AudioFileClip(f"{DEST_AUDIO_ROOT}/{filename}")
            )
        combined_audio = concatenate_audioclips(audios)
        audio_composite = CompositeAudioClip([combined_audio])
        background_clip.audio = audio_composite
        final = CompositeVideoClip([background_clip])
        final.write_videofile(
            f"{DEST_VIDEO_ROOT}/tmp.mp4",
            fps=30,
            audio_codec="aac",
            audio_bitrate="192k",
            verbose=False,
            threads=multiprocessing.cpu_count(),
        )
