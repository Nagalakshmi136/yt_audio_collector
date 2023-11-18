import pytest
from yt_audio_collector.system_1.fetch_youtube_data import FetchValidYouTubeData


@pytest.fixture
def fetch_youtube_data():
    """
    Creating the FetchValidYouTubeData instance

    Parameters:
    ----------- 

    Return:
    -------                 
    'FetchValidYouTubeData'         
        _description_  
    """
    return FetchValidYouTubeData()


def test_get_video_ids(fetch_youtube_data):
    """
    Tests the get_video_ids method.

    Parameters:
    ----------- 
    fetch_youtube_data: `function`
        A function that returns the FetchValidYouTubeData object.
    """
    query = "history_in_hindi"
    video_ids = fetch_youtube_data.get_video_ids(query)
    assert isinstance(video_ids, list)
    assert all(isinstance(video_id, str) for video_id in video_ids)


def test_get_valid_video_ids(fetch_youtube_data):
    """
    Tests the get_valid_video_ids method

    Parameters:
    ----------- 
    fetch_youtube_data: `function`
        A function that returns the FetchValidYouTubeData object.
    """
    query = "history in hindi"
    valid_video_ids = list(fetch_youtube_data.get_valid_video_ids(query))
    assert isinstance(valid_video_ids, list)
    assert all(isinstance(video_id, str) for video_id in valid_video_ids)
    