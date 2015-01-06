#!/bin/bash
set -e
pip install -r /project/requirements.txt
gunicorn things:app
