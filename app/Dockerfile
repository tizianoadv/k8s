FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV MESSAGE="Hello World" \
    APP_PORT="8080"

CMD ["python", "motd-api.py"]
