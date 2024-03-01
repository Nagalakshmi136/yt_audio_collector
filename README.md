# yt_audio_collector

*yt_audio_collector* is a genuine, lightweight library for creating hindi dataset for speech recognition from youtube.

## Documentation

Detailed documentation about the usage of the library can be found at [yt_audio_collector](https://nagalakshmi136.github.io/yt_audio_collector/). This is recommended for most cases. If you want to hastily download a single video, the [quick start](#Quickstart) guide below might be what you're looking for.

## Description

YouTube is the most popular video-sharing platform in the world and as a machine learning engineer or AI engineer, you may encounter a situation where you want to script something to create datasets for training speech recognition models in any 
particular language for this we need audio and transcripts in that language.
For this, I present to you: *yt_audio_collector*.

## Quickstart

This guide covers the most basic usage of the library. For more detailed information, please refer to [yt_audio_collector.io](https://nagalakshmi136.github.io/yt_audio_collector/).

### Installation

yt_audio_collector requires an installation of Python 3.6 or greater, as well as pip. (Pip is typically bundled with Python [installations](https://python.org/downloads).)

To install from PyPI with pip:

```bash
$ python -m pip install yt_audio_collector
```

Sometimes, the PyPI release becomes slightly outdated. To install from the source with pip:

```bash
$ python -m pip install git+https://github.com/Nagalakshmi136/yt_audio_collector
```
### Using yt_audio_collector in a Python script


```python
 >>> from yt_audio_collector.system_1.fetch_youtube_data import FetchValidYouTubeData
 >>> yt_data = FetchValidYouTubeData()
 >>> video_ids = yt_data.get_valid_video_ids('cricket news in hindi')
 >>> from yt_audio_collector.system_2.preprocess_audio import PreProcessAudio
 >>> PreProcessAudio(source_path, destination_path, background_sound).preprocess_audio()
```

## Cloning the repository

Clone the repository through the terminal using the command below:

```shell
git clone https://github.com/Nagalakshmi136/yt_audio_collector.git
```

create conda enviroment with the following command:  

    $ conda create --name yt-collector python=3.9

If poetry not available install poetry:  

    $ sudo apt install poetry

Install required pacakages from poetry with the following command:  

    $ poetry install

To execute the code run the command:

    $ python main.py