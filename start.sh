#!/bin/bash
chmod +x /path/to/start.sh
/start.sh
web: gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT