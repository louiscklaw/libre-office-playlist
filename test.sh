#!/usr/bin/env bash

set -ex

cd /home/logic/.config/libreoffice/4/user/Scripts/tests
  pipenv run python3 ./test.py
cd -