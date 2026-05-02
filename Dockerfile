# Use the official Python lightweight image
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Run the web service on container startup using gunicorn
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 weatherapp.wsgi:application
