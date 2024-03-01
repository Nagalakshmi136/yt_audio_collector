# pylint: disable=import-error, bare-except, consider-using-with
"""
    Collect the youtube data
"""
import json
import re
import urllib.request
from typing import List

from tqdm import tqdm
from youtube_transcript_api import YouTubeTranscriptApi

from yt_audio_collector.constants import BASE_PATH
from yt_audio_collector.system_1.valid_transcript import \
    is_valid_hindi_transcript
from yt_audio_collector.system_1.video_to_audio import has_hindi_audio
from yt_audio_collector.utils.file_utils import create_dir


class FetchValidYouTubeData:
    """
    class to fetch youtube data
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_video_ids(query: str) -> List[str]:
        """
        Fetches all video ids corresponding to the given query from YouTube.

        Parameters:
        -----------
        query: `str`
            The search query.

        Return:
        -------
        List[str]
            A list of video ids fetched from YouTube based on the given query.
        """
        # Replace underscores with plus signs to match YouTube's search query format
        query = query.replace("_", "+")
        total_video_ids = []
        # While requesting the youtube server every time it gives slightly
        # different results for the same query, to capture the majority no.of
        # results request the server multiple times(say 5 here) and
        # and store all the results.
        for _ in range(5):
            # Requests the youtube server using urllib library which gives html file
            # with the following url where sp=EgQoATAB helps to filter the
            # results for the query with the features Subtitles/CC and Creative Commons
            html = urllib.request.urlopen(
                f"https://www.youtube.com/results?search_query={query}&sp=EgQoATAB"
            )
            # html contains the list of youtube video links, by using regex library
            # find all the video ids by matching the video id pattern in total html file
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            total_video_ids.extend(video_ids)
        # Remove duplicates and return unique results(video ids).
        return list(set(total_video_ids))

    def get_valid_video_ids(self, query: str) -> List[str]:
        """
        Finds video ids which have Hindi audio and Hindi transcript from YouTube.

        Parameters:
        -----------
        query: `str`
            The search query.
        status_container: `Container`
            A container to store the status of the program.

        Return:
        -------
        List[str]
            A list of valid video ids.
        """
        # To store files temporarily, here mainly for storing for audio files
        create_dir(BASE_PATH / "temp")
        query = query.replace(" ", "_")
        # Fetch all video ids for the given query
        video_ids = self.get_video_ids(query)
        transcript_results = {}
        for video in tqdm(video_ids):
            try:
                # Fetch the hindi transcript for the video id using youtube_transcript_api library
                transcript_list = YouTubeTranscriptApi.list_transcripts(video)
                transcript = transcript_list.find_manually_created_transcript(
                    language_codes=["hi"]
                )
                video_transcript = transcript.fetch()
                # Check if the transcript is valid
                if is_valid_hindi_transcript(video_transcript, video) is True:
                    # Check if the video has Hindi audio
                    if has_hindi_audio(video, query):
                        transcript_results[video] = video_transcript

            except:
                continue
        # Store the transcripts in a JSON file inside the folder which have audio files
        # for all the transcripts with the query name in audio folder
        if transcript_results:
            with open(
                f"{BASE_PATH}/output/{query}/{query}.json", "w", encoding="utf-8"
            ) as json_file:
                json.dump(transcript_results, json_file, indent=4, ensure_ascii=False)

        # Return the list of valid video ids
        return transcript_results.keys()
