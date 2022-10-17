# Pull python base image
FROM python:3.10.7-alpine

# Set the application directory
WORKDIR /app1-flask

# Install our requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy our code from the current folder to /app1-flask inside the container
COPY . .

# Make port 5000 available for links and/or publish
EXPOSE 5000

# Define Environement
ENV NAME=Minikube

# Define our command to be run when launching the container
CMD ["python", "app.py"]