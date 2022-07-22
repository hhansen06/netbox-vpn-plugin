#!/bin/bash
# Runs on every start of the NetBox Docker container

# Stop when an error occures
set -e

# Allows NetBox to be run as non-root users
umask 002

# Load correct Python3 env
echo "############## Activating VENV ##############"
source /opt/netbox/venv/bin/activate
echo "############## Setup Plugin ##############"
cd /opt/netbox/netbox/netbox-vpn-plugin/
python3 setup.py develop

echo "############## starting manage runserver ##############"
cd /opt/netbox/netbox/

if ! ./manage.py migrate --check >/dev/null 2>&1; then
  echo "⚙️ Applying database migrations"
  ./manage.py migrate --no-input
  echo "⚙️ Running trace_paths"
  ./manage.py trace_paths --no-input
  echo "⚙️ Removing stale content types"
  ./manage.py remove_stale_contenttypes --no-input
  echo "⚙️ Removing expired user sessions"
  ./manage.py clearsessions
fi

cd /opt/netbox/
python3 netbox/manage.py runserver 0.0.0.0:8080 --insecure