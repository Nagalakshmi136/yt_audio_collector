import os
import json
import pytest
from pathlib import Path
from yt_audio_collector.system_2.preprocess_audio import PreProcessAudio


@pytest.fixture
def preprocessed_audio(tmp_path):
    source_path = Path("/home/munikumar/Desktop/hindi_dataset/audio")
    destination_path = tmp_path / "processed_audio"
    background_sound = False
    preprocessed_audio = PreProcessAudio(
        source_path, destination_path, background_sound
    )
    preprocessed_audio.preprocess_audio()
    return preprocessed_audio


def test_get_file_name():
    preprocessed_audio = PreProcessAudio(None, None, None)
    total_file_path = Path("path/to/file.mp3")
    expected_output = "file"
    assert preprocessed_audio.get_file_name(total_file_path) == expected_output


def test_extract_vocals(preprocessed_audio):
    chunk_path = "tests/data/temp/file_0_1000.wav"
    assert os.path.exists(f"{chunk_path}/vocals.wav")


def test_resample(preprocessed_audio):
    chunk_path = "tests/data/temp/file_0_1000"
    destination_chunk_path = "tests/data/processed_audio/file/file_0_1000"
    assert os.path.exists(f"{destination_chunk_path}.wav")


def test_get_audio_chunks(preprocessed_audio):
    category_path = "file"
    destination_category_path = preprocessed_audio.destination_path / category_path
    assert os.path.exists(destination_category_path)
    assert os.path.exists(destination_category_path / "file_0_1000/subtitles.csv")
    assert os.path.exists(destination_category_path / "file_0_1000/file_0_1000.wav")


def test_get_processed_audio(preprocessed_audio):
    processed_audio_file_path = (
        preprocessed_audio.destination_path / "processed_audios.json"
    )
    with open(processed_audio_file_path, "r", encoding="utf-8") as file_reader:
        processed_audios = json.load(file_reader)
    assert processed_audios == {
        "file": ["file"]
    }  # assuming there's only one file in the test data
