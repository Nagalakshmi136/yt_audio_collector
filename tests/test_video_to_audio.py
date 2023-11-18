import os
from pathlib import Path
from unittest.mock import patch

import pytest
import whisper

from yt_audio_collector.system_1.video_to_audio import (
    BASE_PATH,
    convert_video_to_audio,
    duration_of_video,
    has_hindi_audio,
    store_audio,
)


@pytest.fixture
def video_id():
    """
    Sample video ID for testing.
    
    Return:
    -------                 
    `str`
        Sample video ID for testing           
    """
    return "x0YnzXlwQSY"


@pytest.fixture
def query():
    """
    Sample query for testing.

    Parameters:
    ----------- 

    Return:
    -------                 
    `str`         
        Sample query for testing.  
    """
    return "finance in hindi"


@pytest.fixture
def audio_file(tmp_path):
    """
    Create temporary audio file.

    Parameters:
    ----------- 
    tmp_path: `function`
        A function returns a valid path.
    """
    # create temporary audio file
    audio_path = tmp_path / "audio.mp3"
    with open(audio_path, "w",encoding='UTF-8') as file_writer:
        file_writer.write("test audio")
    yield audio_path
    # remove temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)


@pytest.fixture
def temp_dir(tmp_path):
    """
    Create temporary directory
    
    Parameters:
    ----------- 
    tmp_path: `function`
        A function returns a valid path.
    """
    # create temporary directory
    temp_path = tmp_path / "temp"
    temp_path.mkdir()
    yield temp_path
    # remove temporary directory
    if os.path.exists(temp_path):
        os.rmdir(temp_path)


@pytest.fixture
def whisper_model():
    """
    mock whisper model
    """
    with patch.object(whisper, "load_model") as mock_load_model:
        mock_model = mock_load_model.return_value
        mock_model.device = "cpu"
        mock_model.detect_language.return_value = ("hi", {"hi": 0.9, "en": 0.1})
        yield mock_model


def test_duration_of_video(video_id):
    """
    Tests duration_of_video function.

    Parameters:
    ----------- 
    video_id: `function`
        A function returns video_id.
    """
    duration = duration_of_video(video_id)
    assert isinstance(duration, int)
    assert duration > 0


def test_convert_video_to_audio(video_id):
    """
    test convert_video_to_audio function.

    Parameters:
    ----------- 
    video_id: `function`
        A function returns video_id.
    """
    audio_file = convert_video_to_audio(video_id)
    assert isinstance(audio_file, Path)
    assert audio_file.exists()
    assert audio_file.suffix == ".mp3"


def test_store_audio(query, audio_file):
    """
    Test store_audio function.
    
    Parameters:
    ----------- 
    query: `function`
        A function returns search query.
    audio_file: `function`
        A function creates temporary audio file.
    """
    store_audio(query, audio_file)
    destination_path = BASE_PATH / "output" / query.replace(" ", "_") / audio_file.name
    assert destination_path.exists()


@pytest.mark.parametrize(
    "audio_language, expected_result",
    [("hi", True), ("en", False), ("fr", False)],
)
def test_has_hindi_audio(
    video_id, query, audio_language, expected_result, whisper_model):
    """
    Test has_hindi_audio function with parameterization.
    
    Parameters:
    ----------- 
    video_id: `function`
        A function returns video_id.
    query: `function`
        A function returns search query.
    audio_language: `Literal`
        audio language.
    expected_result: `bool`
        Expected result.
    whisper_model: `function`
         mock whisper model.
    """
    whisper_model.detect_language.return_value = (audio_language, {audio_language: 0.9})
    result = has_hindi_audio(video_id, query)
    assert result == expected_result
    if result:
        destination_path = BASE_PATH / "output" / query.replace(" ", "_") / f"{video_id}.mp3"
        assert destination_path.exists()
    else:
        audio_file = BASE_PATH / "temp" / f"{video_id}.mp3"
        assert not audio_file.exists()
        