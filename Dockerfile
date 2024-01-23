FROM python:3.8-slim


ARG DOCKERHUB_USERNAME
ARG DOCKER_PASSWORD
ARG DB_PASSWORD

ENV DOCKERHUB_USERNAME=${DOCKERHUB_USERNAME}
ENV DOCKER_PASSWORD=${DOCKER_PASSWORD}
ENV DB_PASSWORD=${DB_PASSWORD}
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN cat /home/runner/.docker/config.json

EXPOSE 80

CMD ["python", "main.py"]
