"""
This module contains functions to convert YouTube videos to audio files, detect the language of the audio,
store the audio files, and check if the audio is in Hindi language.
"""

import os
from pathlib import Path

import whisper
from pytube import YouTube

from constants import BASE_PATH, BASE_URL


def get_audio_language(audio_path: str) -> str:
    """
    Detects the language of an audio using the whisper model.

    Parameters:
    -----------
    audio_path: `str`
        The path of the audio file.

    Return:
    -------
    str
        The language of the given audio.
    """

    model = whisper.load_model("base")
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    return detected_language

def duration_of_video(video_id: str) -> int:
    """
    Gets the duration of the video in seconds using the pytube library.

    Parameters:
    -----------
    video_id: `str`
        The id of the video.

    Return:
    -------
    int
        The duration of the video in seconds.
    """
    yt = YouTube(f"{BASE_URL}{video_id}")
    return yt.length


def store_audio(query: str, audio_path: Path) -> None:
    """
    Stores the audio file in a separate audio folder.

    Parameters:
    -----------
    query: `str`
        Represents the data you need.
    audio_path: `Path`
        The path of the audio file.
    """
    destination_path = BASE_PATH / "audio" / query.replace(" ", "_") / audio_path.name
    if not destination_path.parent.exists():
        destination_path.parent.mkdir(parents=True)
    os.replace(audio_path, destination_path)


def convert_video_to_audio(video_id: str) -> Path:
    """
    Converts a video to an audio file.

    Parameters:
    -----------
    video_id: `str`
        The id of the video.

    Return:
    -------
    Path
        The path of the converted audio file.
    """
    url = f"{BASE_URL}{video_id}"
    you_tube = YouTube(url)
    try:
        # Fetching the audio of the video with given id
        video = you_tube.streams.filter(only_audio=True).first()
    except Exception as exception:
        print(exception)
    destination = BASE_PATH / "temp"
    # Downloading the audio in temporary file and it gives audio file
    # but with mp4(video supported format) extension which we need to
    # convert to mp3(audio supported format)
    output_file = video.download(output_path=destination)
    # Renaming the downloaded file with mp3
    new_file = destination / f"{video_id}.mp3"
    os.rename(output_file, new_file)
    return new_file


def has_hindi_audio(video_id: str, query: str) -> bool:
    """
    Converts the video to an audio file, determines its audio language,
    stores the audio file if it's in Hindi language, and returns True.
    Otherwise, removes the audio file and returns False.

    Parameters:
    -----------
    video_id: `str`
        The id of the video.
    query: `str`
        Represents the data you need.

    Return:
    -------
    bool
        True if the audio language is Hindi, and False otherwise.
    """
    audio_file = convert_video_to_audio(video_id)
    audio_language = get_audio_language(audio_file)
    print(audio_language)

    if audio_language.lower() in ["hi"]:
        store_audio(query, audio_file)
        return True
    # Removing the audio file which is not Hindi from temporary storage
    if os.path.exists(audio_file):
        os.remove(audio_file)
    return False
