# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /var/www/html/src

# Copy code
COPY ./src /var/www/html/src

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Cloud Run uses
EXPOSE 8080

# Start using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
