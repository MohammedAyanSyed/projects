# Base Image
FROM python:3.12-slim

# WORKING Directory
WORKDIR /app

# Requirements and dependepencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY Project FIles
COPY . .

# Application Port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn","app.Fast_API:app","--host","0.0.0.0","--port","8000"]