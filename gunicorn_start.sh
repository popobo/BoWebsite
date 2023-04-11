#!/bin/bash

NAME="BoWebsite"                                  # Name of the application
DJANGODIR=/home/ubuntu/code/BoWebsite          # Django project directory
SOCKFILE=/home/ubuntu/code/BoWebsite/run/gunicorn.sock  # Gunicorn socket
USER=ubuntu                                       # User to run as
GROUP=ubuntu                                     # Group to run as
NUM_WORKERS=3                                     # Number of Gunicorn workers
DJANGO_SETTINGS_MODULE=BoWebsite.settings         # Django settings module
DJANGO_WSGI_MODULE=BoWebsite.wsgi                 # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start Gunicorn
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=- \
  --access-logfile $DJANGODIR/gunicorn_logs/log_file.log \
  --error-logfile $DJANGODIR/gunicorn_logs/error_file.log
