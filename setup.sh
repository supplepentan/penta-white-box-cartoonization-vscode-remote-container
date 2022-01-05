#!/bin/bash
apt install ffmpeg
mkdir "test_video"
pip install -U pip setuptools
pip install -r requirements.txt
pip install nvidia-pyindex
pip install nvidia-tensorflow[horovod]