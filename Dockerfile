# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install Flask
RUN pip install Flask

# Copy the working application code
COPY app_working.py .

# Command to run the app
# Cloud Run will set the $PORT environment variable
CMD ["python", "app_working.py"]