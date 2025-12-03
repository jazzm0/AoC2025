#!/usr/bin/env bash

rm -Rf env && \
pyenv install 3.12.8 || \
pyenv global 3.12.8 && \
python3.12 -m venv env && \
source env/bin/activate && \
pip install --upgrade pip && \
echo "" && \
echo "Setup on *unix system finished, ready to run some tests" && \
echo ""
