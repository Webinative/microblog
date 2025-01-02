#!/bin/bash

# This script is used to initialize the application for development environment.
# Usage: docker-compose exec microblog-django bash init_alpha.sh

# Apply database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser --noinput

python manage.py shell < alpha_env/01_posts.py
