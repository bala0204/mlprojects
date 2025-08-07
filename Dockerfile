FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

RUN apt update -y && apt install awscli -y
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD ["python3", "app.py"]
