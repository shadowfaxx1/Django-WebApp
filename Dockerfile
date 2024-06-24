FROM python:3.11.3-slim

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential gcc

WORKDIR /app

# Copy requirements and install dependencies as root
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create non-root user
RUN adduser --disabled-password --gecos "" --home "/nonexistent" --shell "/sbin/nologin" --no-create-home --uid "10001" appuser

# Copy the application code and change ownership to the non-root user
COPY . .
RUN chown -R appuser /app

# Switch to non-root user
USER appuser

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
