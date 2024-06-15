#!/bin/bash
set -e

# Create pg_notify directory if it doesn't exist
mkdir -p /var/lib/postgresql/data/pg_notify

# Execute the original entrypoint script
exec docker-entrypoint.sh "$@"
