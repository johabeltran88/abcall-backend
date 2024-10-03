FROM python:3.12.2

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV FLASK_APP=main.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["flask", "run"]