#!/bin/bash

# install dependencies
pip install -r requirements.txt

# run the app
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
