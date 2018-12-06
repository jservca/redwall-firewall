#!/bin/bash
source ../../venv/bin/activate
export FLASK_APP=webserver.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0 --port 8122
