# Use the official Ubuntu as the base image
FROM ubuntu:20.04

# Set environment variables to non-interactive mode during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary packages
RUN apt-get update -y && \
    apt-get install -y \
    software-properties-common \
    python3 \
    python3-pip

# Install any dependencies for your demo application (replace with your app's dependencies)
# RUN apt-get install -y <your-dependencies>

# Copy your demo application code into the container
COPY . /app

# Set the working directory to your application's directory
WORKDIR /app

# Expose the port your application is listening on (replace with the actual port)
EXPOSE 80

# Start your demo application (replace with the actual command)
CMD ["python3", "app.py"]
