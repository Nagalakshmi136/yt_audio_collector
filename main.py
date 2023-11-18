# pylint: disable = missing-module-docstring
from yt_audio_collector.system_1.fetch_youtube_data import FetchValidYouTubeData
from yt_audio_collector.system_2.preprocess_audio import PreProcessAudio

yt_data = FetchValidYouTubeData()
video_ids = yt_data.get_valid_video_ids("cricket news in hindi")
PreProcessAudio().preprocess_audio()
