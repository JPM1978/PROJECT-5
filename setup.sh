#!/usr/bin/env bash



set -0 errexit

pip install -r dependencies.txt

#run migration
python3 manage.py migrate