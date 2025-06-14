FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install --force-reinstall dagshub==0.3.24

# Copy .env file early so it’s available before code runs
COPY .env .env

# Copy source code
COPY . .

# Expose FastAPI port
EXPOSE 10000

# Run FastAPI app
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "10000"]
