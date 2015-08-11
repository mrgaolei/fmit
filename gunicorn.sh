#! /bin/bash

gunicorn -D -b unix:./sock_gunicorn.sock -w 2 -p ./pid_gunicorn.pid fmit.wsgi
