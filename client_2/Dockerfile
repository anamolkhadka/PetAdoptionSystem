# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.9.13
FROM python:${PYTHON_VERSION}-slim as base

# Prevent Python from writing pyc files and buffer stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the rest of the source code
COPY . .

# Run the application
CMD ["python3", "client.py"]
