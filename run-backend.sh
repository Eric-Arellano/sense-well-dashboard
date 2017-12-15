#!/usr/bin/env bash
source backend/bin/activate
export FLASK_APP=backend/src/app.py
flask run
