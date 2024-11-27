#!/bin/sh

#encerra se o script se algo falhar
set -e

python /application/portalUEMG/manage.py runserver 0.0.0.0:8000
