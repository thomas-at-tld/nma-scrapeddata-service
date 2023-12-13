# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Build arguments
ARG MONGO_HOST
ARG MONGO_USERNAME
ARG MONGO_PASSWORD

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

# Define environment variable
ENV MONGO_HOST=$MONGO_HOST
ENV MONGO_USERNAME=$MONGO_USERNAME
ENV MONGO_PASSWORD=$MONGO_PASSWORD
ENV NAME nma-scrapeddata-service

# Run app.py when the container launches
CMD ["python", "app.py"]