# pylint: disable=redefined-outer-name
import os

import pytest

from yt_audio_collector.constants import BASE_PATH
from yt_audio_collector.system_2.preprocess_audio import PreProcessAudio


@pytest.fixture
def audio_preprocessor():
    """
    Creates a PreProcessAudio object.
    
    Return:
    -------                 
    'PreprocessAudio'           
    """
    source_path = BASE_PATH.parent / "output"
    destination_path = BASE_PATH.parent / "processed_output"
    background_sound = False
    return PreProcessAudio(
        source_path,
        destination_path,
        background_sound,
    )


def test_preprocess_audio(audio_preprocessor: PreProcessAudio):
    """
    Tests the results of preprocess_audio method

    Parameters:
    ----------- 
    audio_preprocessor: `function`
        It is a function returns the PreProcessAudio instance
    """
    audio_preprocessor.preprocess_audio()
    # Check if the destination directory exists
    assert os.path.exists(audio_preprocessor.destination_path)
    print(os.path.exists(audio_preprocessor.destination_path))
    # Check if the processed_audios.json file exists
    assert os.path.exists(
        os.path.join(audio_preprocessor.destination_path, "processed_audios.json")
    )
    # Check if the audio files have been processed and saved in the destination directory
    assert len(os.listdir(audio_preprocessor.destination_path)) > 0
