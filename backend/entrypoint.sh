#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Seed data
echo "Seeding data..."
python seed_gesp_courses.py

# Start server
echo "Starting server..."
exec "$@"
