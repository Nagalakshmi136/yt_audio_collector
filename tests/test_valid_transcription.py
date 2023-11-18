#pylint: disable=singleton-comparison
import pytest

from yt_audio_collector.system_1.valid_transcript import is_valid_hindi_transcript


@pytest.fixture
def transcript():
    """
    Sample transcript for testing

    Parameters:
    ----------- 

    Return:
    -------                 
    `List[dict]`         
        Sample transcript for testing 
    """
    return [
        {
            "text": "के बैकग्राउंड में बज रहे म्यूजिक को\nज्यादा तो फैक्ट्री यूट्यूब चैनल्स",
            "start": 0.0,
            "duration": 2.939
        },
        {
            "text": "म्यूजिक को यूज करते हुए वीडियो में लेकिन\nयह YouTube पर से जिनको यह म्यूजिक तो",
            "start": 2.939,
            "duration": 4.38
        },
        {
            "text": "चाहिए लेकिन उसका नाम ही नहीं पता आपको\nबता दूं कि म्यूजिक शॉर्ट वीडियो में सबसे",
            "start": 7.319,
            "duration": 4.11
        },
        {
            "text": "ज्यादा यूज की जाने वाला म्यूजिक है और\nइसको ज्यादातर फैट चैनल ही यूज करते हैं",
            "start": 11.429,
            "duration": 4.41
        },
        {
            "text": "अपनी वीडियो में अगर आपको इस म्यूजिक का\nनाम नहीं पता तो मैं आपको बता देता हूं इस",
            "start": 15.839,
            "duration": 4.171
        },
        {
            "text": "म्यूजिक आना में हिंदी काउंट डाउन जिसकी\nलिंक आपको डिस्क्रिप्शन के अंदर मिल जाएगी",
            "start": 20.01,
            "duration": 4.47
        },
        {
            "text": "तो आप भी जाकर लिंक के जरिए ऐप डाउनलोड कर\nसकते हो और अपनी वीडियो में यूज कर सकते",
            "start": 24.48,
            "duration": 4.44
        },
        {
            "text": "हो ऐसे अमेजिंग वीडियोस के लिए हमें\nसब्सक्राइब भी कर सकते हो",
            "start": 28.92,
            "duration": 5.69
        }
    ]


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


def test_valid_hindi_transcript(transcript, video_id):
    """
    Test a valid Hindi transcript.

    Parameters:
    ----------- 
    transcript: `List[dict]`
        sample transcript for the audio file.
    video_id: `str`
        sample audio file.
    """
    # Test a valid Hindi transcript
    assert is_valid_hindi_transcript(transcript, video_id) == True


def test_invalid_hindi_transcript_empty_text(transcript, video_id):
    """
    Test an invalid Hindi transcript with too many empty texts.
    
    Parameters:
    ----------- 
    transcript: `List[dict]`
        sample transcript for the audio file.
    video_id: `str`
        sample audio file.
    """
    for i in range(5):
        transcript[i]['text'] = ""
    assert is_valid_hindi_transcript(transcript, video_id) == False


def test_invalid_hindi_transcript_no_hindi(transcript, video_id):
    """
    Test an invalid Hindi transcript with no Hindi text

    Parameters:
    ----------- 
    transcript: `List[dict]`
        sample transcript for the audio file.
    video_id: `str`
        sample audio file.
    """
    for i in enumerate(transcript):
        transcript[i]["text"] = "This is a English text"
    assert is_valid_hindi_transcript(transcript, video_id) == False


def test_invalid_hindi_transcript_no_duration(transcript, video_id):
    """
    Test an invalid Hindi transcript with missing duration
    
    Parameters:
    ----------- 
    transcript: `List[dict]`
        sample transcript for the audio file.
    video_id: `str`
        sample audio file.
    """
    transcript[0].pop("duration")
    with pytest.raises(TypeError):
        is_valid_hindi_transcript(transcript, video_id)
        