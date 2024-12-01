#Student Name-Rishita Sadhwani
#Student Id-1234157173
#Date-November 11 ,2024
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ..
CMD ["python","app.py"]