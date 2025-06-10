# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#  Install dotenv explicitly if needed (optional safety)
RUN pip install python-dotenv

#  Copy .env file
COPY .env .

# Optional but recommended: set the environment variable inside container
# This ensures the DAGSHUB_TOKEN is accessible inside the container
ENV DAGSHUB_TOKEN=${DAGSHUB_TOKEN}

# Copy all project files
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
