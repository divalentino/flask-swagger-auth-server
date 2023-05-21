#!/bin/bash

gunicorn "swagger_server.wsgi:app" -w 4 -b 0.0.0.0:8080
