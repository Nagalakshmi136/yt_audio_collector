.. _install:

Installation of yt_audio_collector:
===================================

This guide assumes you already have python and pip installed.

To install yt_audio_collector, run the following command in your terminal::

    $ pip install yt_audio_collector

Get the Source Code
-------------------

yt_audio_collector is actively developed on GitHub, where the source is `available <https://github.com/Nagalakshmi136/yt_audio_collector>`_.

You can either clone the public repository::

    $ git clone https://github.com/Nagalakshmi136/yt_audio_collector.git

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running::

    $ cd yt_audio_collector
    
After cloning create an environment then install python=3.9 version. For example with conda::

    $ conda create -n sample python=3.9

To install all the libraries in the pyproject.toml file of a cloned project, you should run the following command::

    $ poetry install

To execute the code run the command::

    $ python main.py