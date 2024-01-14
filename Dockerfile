FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
ARG DB_PASSWORD
ENV DB_PASSWORD=${{ secrets.DB_PASSWORD }}

# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["python", "main.py"]
