#!/bin/bash
set -e

python3 generate_config.py &
/usr/local/bin/xray run -config /etc/xray/config.json &
uvicorn main:app --host 0.0.0.0 --port 80