#refered based image from: https://hub.docker.com/_/python
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

#copy current directory into docker container
COPY . .

# Install necessary libraries
RUN pip install --upgrade pip && pip install -r requirements.txt

# When the container starts, run "python app.py"
CMD ["python", "app.py"]