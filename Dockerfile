FROM python:3.11-slim-buster

WORKDIR /usr/src/app

RUN --mount=type=bind,src=.,dst=. \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "app.py" ]
