# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /ghg

ARG RUN_ENV=prod
RUN pip install -U pip

ADD requirements.txt /ghg/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /ghg

ADD ghg.sh /ghg/
RUN chmod 0755 ghg.sh

# Make port 80 available to the world outside this container
EXPOSE 8888
