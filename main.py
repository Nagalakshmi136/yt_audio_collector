from yt_audio_collector.system_1.fetch_youtube_data import FetchValidYouTubeData
from yt_audio_collector.system_2.preprocess_audio import PreProcessAudio
# from src.yt_audio_collector.constants import BASE_PATH

yt_data = FetchValidYouTubeData()
video_ids = yt_data.get_valid_video_ids('finance in hindi')

preprocess_audio = PreProcessAudio().preprocess_audio()
