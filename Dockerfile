FROM python:3.9

ENV POSTGRES_DB=${DATABASE_NAME}
ENV POSTGRES_USER=${DATABASE_USERNAME}
ENV POSTGRES_PASSWORD=${DATABASE_PASSWORD}
ENV POSTGRES_HOST=${DATABASE_HOSTNAME}
ENV POSTGRES_PORT=${DATABASE_PORT}

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
