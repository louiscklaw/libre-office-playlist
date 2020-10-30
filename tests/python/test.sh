#!/usr/bin/env bash

set -ex

cd /home/logic/.config/libreoffice/4/user/Scripts/tests/python
  # pipenv sync
  # pipenv install requests
  nodemon --delay 2 -w . -e "sh,js,html,css,scss,sass,yml,py" --ignore './node_modules' --ignore './public' --ignore './reports'  --delay 500ms --exec "pipenv run python3 ./test.py"

cd -
