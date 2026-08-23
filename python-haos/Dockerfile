FROM ghcr.io/home-assistant/base:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv /app/.venv
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

COPY app.py /app/app.py
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]
