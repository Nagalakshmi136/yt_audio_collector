from src.yt_audio_collector.system_1.fetch_youtube_data import FetchValidYouTubeData
from src.yt_audio_collector.system_2.preprocess_audio import PreProcessAudio
from constants import BASE_PATH
# yt_data = FetchValidYouTubeData()
# video_ids = yt_data.get_valid_video_ids('finance in hindi')

preprocess_audio = PreProcessAudio(
                        f"{BASE_PATH}/audio", f"{BASE_PATH}/processed_audio", False
                    ).preprocess_audio()
