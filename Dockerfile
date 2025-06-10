# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# Upgrade pip and reinstall all packages (including fixing dagshub version)
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir --force-reinstall -r requirements.txt

# Copy all project files
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
