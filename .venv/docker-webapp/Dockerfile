FROM python:3.9-slim

WORKDIR /app  

# Copy requirements.txt from your local machine to the /app directory in the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files from the local folder to the /app directory in the container
COPY . /app

# Set the default command to run your app
CMD ["python", "server.py"]
