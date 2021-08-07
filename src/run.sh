#! /bin/bash
sudo apt install gunicorn3
gunicorn3 --bind=0.0.0.0:5000 app:app