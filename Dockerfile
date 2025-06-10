# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run FastAPI app (api is your app instance in app.py)
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
