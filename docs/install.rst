.. _install:

Installation of yt_audio_collector:
===================================

This guide assumes you already have python and pip installed.

To install yt_audio_collector, run the following command in your terminal::

    $ pip install yt_audio_collector

Get the Source Code
-------------------

yt_audio_collector is actively developed on GitHub, where the source is `available <https://github.com/Nagalakshmi136/yt_audio_collector>`_.

Clone the repository through the terminal using the command below::

    $ git clone https://github.com/Nagalakshmi136/yt_audio_collector.git

create conda enviroment with the following command::  

    $ conda create --name yt-collector python=3.9

If poetry not available install poetry::

    $ sudo apt install poetry

Install required pacakages from poetry with the following command::

    $ poetry install

To execute the code run the command::

    $ python main.py