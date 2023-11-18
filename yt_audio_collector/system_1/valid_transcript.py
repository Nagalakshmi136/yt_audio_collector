"""
    Methods to validate transcription
"""
import re
from typing import List

from yt_audio_collector.constants import HINDI_RE_PATTERN
from yt_audio_collector.system_1.video_to_audio import duration_of_video


def is_valid_hindi_transcript(transcript: List[dict], video_id: str) -> bool:
    """
    Checks if the given transcript is valid:
    1. The transcript must be in Hindi.
    2. Exists for the full video without empty text.

    Parameters:
    -----------
    transcript: `List[dict]`
        A list of transcriptions of a video.
    video_id: `str`
        The ID of the video.

    Return:
    -------
    bool
        True if the transcript is valid, False otherwise.
    """
    transcript_length = len(transcript)
    empty_text_count = 0
    hindi_to_total_text_ratio = 0
    subtitles_duration = 0
    for i in range(transcript_length):
        transcript_text = transcript[i].get("text")
        # Check for empty transcript text
        if re.sub(r"[\s]+", "", transcript_text) == "":
            empty_text_count += 1
            # If there are more than 10 empty texts, the transcript is invalid
            if empty_text_count > 10:
                return False
            continue
        # Find all hindi characters in single transcript text
        hindi_chars = re.findall(HINDI_RE_PATTERN, transcript_text)
        len_hindi_chars = len(hindi_chars)
        len_total_chars = len(transcript_text)
        subtitles_duration += transcript[i].get("duration")
        # Calculate the ratio of Hindi characters to total characters
        # of transcript
        if hindi_to_total_text_ratio == 0:
            hindi_to_total_text_ratio = round(len_hindi_chars / len_total_chars, 4)
        else:
            hindi_to_total_text_ratio = round(
                (hindi_to_total_text_ratio + len_hindi_chars / len_total_chars) / 2, 4
            )
    # Check if subtitles duration is < 50% of total duration of video then transcript is invalid
    if subtitles_duration < 0.5 * duration_of_video(video_id):
        return False
    # Check if the ratio of Hindi characters to total characters < 40% then transcript is invalid
    if hindi_to_total_text_ratio * 100 < 40:
        return False
    # If all checks pass, the transcript is valid
    return True
