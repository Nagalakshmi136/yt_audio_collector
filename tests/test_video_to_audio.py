import os
from pathlib import Path
from unittest.mock import patch

import pytest
import whisper

from yt_audio_collector.system_1.video_to_audio import (
    BASE_PATH,
    BASE_URL,
    convert_video_to_audio,
    duration_of_video,
    get_audio_language,
    has_hindi_audio,
    store_audio,
)


@pytest.fixture
def video_id():
    return "x0YnzXlwQSY"


@pytest.fixture
def query():
    return "finance in hindi"


@pytest.fixture
def audio_file(tmp_path):
    # create temporary audio file
    audio_path = tmp_path / "audio.mp3"
    with open(audio_path, "w") as f:
        f.write("test audio")
    yield audio_path
    # remove temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)


@pytest.fixture
def temp_dir(tmp_path):
    # create temporary directory
    temp_path = tmp_path / "temp"
    temp_path.mkdir()
    yield temp_path
    # remove temporary directory
    if os.path.exists(temp_path):
        os.rmdir(temp_path)


@pytest.fixture
def whisper_model():
    # mock whisper model
    with patch.object(whisper, "load_model") as mock_load_model:
        mock_model = mock_load_model.return_value
        mock_model.device = "cpu"
        mock_model.detect_language.return_value = ("hi", {"hi": 0.9, "en": 0.1})
        yield mock_model


def test_duration_of_video(video_id):
    # test duration_of_video function
    duration = duration_of_video(video_id)
    assert isinstance(duration, int)
    assert duration > 0


def test_convert_video_to_audio(video_id, temp_dir):
    # test convert_video_to_audio function
    audio_file = convert_video_to_audio(video_id)
    assert isinstance(audio_file, Path)
    assert audio_file.exists()
    assert audio_file.suffix == ".mp3"


def test_store_audio(query, audio_file):
    # test store_audio function
    store_audio(query, audio_file)
    destination_path = BASE_PATH / "output" / query.replace(" ", "_") / audio_file.name
    assert destination_path.exists()


@pytest.mark.parametrize(
    "audio_language, expected_result",
    [("hi", True), ("en", False), ("fr", False)],
)
def test_has_hindi_audio(
    video_id, query, audio_language, expected_result, whisper_model, temp_dir
):
    # test has_hindi_audio function with parameterization
    whisper_model.detect_language.return_value = (audio_language, {audio_language: 0.9})
    result = has_hindi_audio(video_id, query)
    assert result == expected_result
    if result:
        destination_path = BASE_PATH / "output" / query.replace(" ", "_") / f"{video_id}.mp3"
        assert destination_path.exists()
    else:
        audio_file = BASE_PATH / "temp" / f"{video_id}.mp3"
        assert not audio_file.exists()