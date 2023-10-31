.. _quickstart:

Quickstart
==========

This guide will walk you through the basic usage of hindi-dataset.

Let's get started with some examples.

Preparing the Hindi transcript and audio
----------------------------------------

Begin with importing the fetch_youtube_data module from the 
hindi_dataset/yt_audio_collector/transcript_audio module::
    
    >>> from hindi_dataset.yt_audio_collector.transcript_audio import fetch_youtube_data

Fetch_youtube_data contains a method get_valid_video_ids 
helps to get the video IDs that have Hindi audio and Hindi transcript of the
relevant videos for the given query and store the Hindi transcript and Hindi audio
with the query name inside the audio folder in the current project::

    >>> video_ids = fetch_youtube_data.get_valid_video_ids('cricket news in hindi')

Preprocessing Hindi audio
-------------------------
Begin with importing PreProcessAudio class from hindi_dataset/yt_audio_collector/system_2/preprocess_audio::

    >>> from hindi_dataset.yt_audio_collector.system_2.preprocess_audio import PreProcessAudio

To preprocessing the Hindi audio stored in audio folder, Use the preprocess_audio method of PreProcessAudio class
which take 3 arguments:

1. Source location of the audio files which need to be process.
2. Destination location of the audio files after preprocessing.
3. Enable or Disable the background sound(default value is False(Enable)).

    >>> PreProcessAudio(source_path, destination_path, background_sound).preprocess_audio()

.. admonition:: Remember!

   For disabling the background sound of the audio we need to use the spleeter library
   which can be installed with:

       $ pip install spleeter

   This spleeter library only supports the older version of protobuf library(i.e. 3.2 or lower) which can be installed with:

       $ pip install protobuf==3.2
        





