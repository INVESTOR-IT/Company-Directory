FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN echo "deb http://ftp.debian.org/debian trixie main" > /etc/apt/sources.list \
    && echo "deb http://ftp.debian.org/debian trixie-updates main" >> /etc/apt/sources.list \
    && echo "deb http://security.debian.org/debian-security trixie-security main" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]