# Use an official Python runtime as the parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copier d'abord le fichier de dépendances
COPY requirements-api.txt .

# Installer les paquets nécessaires
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements-api.txt

# Copier le reste du dossier actuel dans le conteneur à /app
COPY . /app

# Make port 5075 available to the world outside this container
EXPOSE 5075

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Run mnist_api.py when the container launches
CMD ["python", "mnist_api.py", "--model_path", "weights/mnist_net.pth"]