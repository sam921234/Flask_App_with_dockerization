# Use the official Python 3.12.3 image from the Docker Hub
FROM python:3.12.3-slim

# Set the working directory inside the container
WORKDIR /flask-docker

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy requirements.txt to ensure all package dependencies are met
COPY requirements.txt requirements.txt

# Read the content inside requirements.txt and install them
RUN pip3 install -r requirements.txt

# Copy all the files in local machine to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py  
# Run app when the container launches
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
