# Use an official Python image
FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache better
COPY requirements.txt .

# Upgrade pip and FORCE dagshub reinstall
RUN pip install --upgrade pip \
 && pip uninstall -y dagshub \
 && pip install --no-cache-dir dagshub==0.3.24 \
 && pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]
