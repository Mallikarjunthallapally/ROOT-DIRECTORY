# Use an official Python runtime as a parent image
FROM python:3.12.10s-lim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and dependencies
RUN pip install --trusted-host pypi.python.org Flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
