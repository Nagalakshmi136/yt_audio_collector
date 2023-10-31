.. _quickstart:

Quickstart
==========

This guide will walk you through the basic usage of yt_audio_collector.

Let's get started with some examples.

yt_audio_collector contains 2 systems.

The system-1 is used for:

Preparing the Hindi transcript and audio from youtube
-----------------------------------------------------

Begin with importing the FetchValidYouTubeData class from the 
yt_audio_collector/system_1/fetch_youtube_data module::
    
    >>> from yt_audio_collector.system_1.fetch_youtube_data import FetchValidYouTubeData

FetchValidYouTubeData class contains a method get_valid_video_ids 
helps to get the video IDs that have Hindi audio and Hindi transcript of the
relevant videos for the given query and store the Hindi transcript and Hindi audio
with the video id as name of the audio file inside the query as folder name in the output folder of the current project::

    >>> yt_data = FetchValidYouTubeData()
    >>> video_ids = yt_data.get_valid_video_ids('cricket news in hindi')

The system 2 is used for:

Preprocessing Hindi audio
-------------------------
Begin with importing PreProcessAudio class from yt_audio_collector/system_2/preprocess_audio::

    >>> from yt_audio_collector.system_2.preprocess_audio import PreProcessAudio

To preprocessing the Hindi audio stored in audio folder, Use the preprocess_audio method of PreProcessAudio class
which take 3 arguments:

1. Source location of the audio files which need to be process(default value is the path to the output folder which is the result of system-1 module).
2. Destination location of the audio files after preprocessing(default value is the path to the result as shown in processed_output in current working project).
3. Enable or Disable the background sound(default value is False(Enable)).

    >>> PreProcessAudio(source_path, destination_path, background_sound).preprocess_audio()

Now the preprocessed audio stored in destination_path or processed_output folder in current
working project as default.





