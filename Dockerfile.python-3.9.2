#
# docker_flask - Docker setup to start a Flask project.
# Copyright (c) 2020 Paulo Vital <paulo@vital.eng.br>
#

# Set the base image following recommendation from
# https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.9.2-slim-buster

# Basic and general settings
LABEL maintainer="paulo@vital.eng.br"
ENV PYTHONUNBUFFERED 1

# Copy configuration files and install requirements
RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt

# Copy application files
RUN mkdir /app
WORKDIR /app

# Setup necessary variables and execute application
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["-m", "flask", "run", "--host=0.0.0.0"]