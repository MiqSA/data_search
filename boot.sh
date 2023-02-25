#!/bin/bash

gunicorn --workers=4 server:server --bind :8000