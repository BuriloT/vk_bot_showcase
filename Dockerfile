FROM python:3.9-slim

WORKDIR /bot

COPY requirements.txt /bot

RUN pip3 install -r /bot/requirements.txt --no-cache-dir

COPY ./ /bot

CMD ["python", "main.py"]
