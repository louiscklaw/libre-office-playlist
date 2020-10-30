#!/usr/bin/env bash

set -ex

cd /home/logic/.config/libreoffice/4/user/Scripts/python_test
  # pipenv sync
  pipenv run python3 ./test_yahoo_finance.py
