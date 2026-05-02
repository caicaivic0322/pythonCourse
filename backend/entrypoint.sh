#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Seed data
echo "Seeding course data..."
python seed_gesp_courses.py

echo "Seeding exam data..."
python seed_exams.py

if [ "${AUTO_CREATE_SUPERUSER:-true}" = "true" ]; then
  echo "Creating superuser..."
  python create_superuser.py
fi

# Start server
echo "Starting server..."
exec "$@"
