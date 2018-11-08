#!/bin/bash
source ../../venv/bin/activate
export FLASK_APP=webserver.py
export FLASK_DEBUG=1
flask run --port 8122
