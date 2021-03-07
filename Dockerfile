FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --no-cache add --virtual .build-deps wget \
                                            gcc \
                                            build-base \
                                            linux-headers \
                                            libffi-dev
RUN apk --no-cache add openssl-dev cargo libressl-dev musl-dev libffi-dev
RUN pip install -U --force-reinstall pip
RUN python -m pip install --upgrade pip
RUN wget https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py &&\
    python get-poetry.py &&\
    rm -f get-poetry.py

ENV PATH="/root/.poetry/bin:${PATH}"

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN poetry install --no-dev --no-interaction --no-ansi

RUN apk --no-cache del --purge .build-deps

COPY . /app
COPY .env /app

EXPOSE 80
ENTRYPOINT ["poetry", "run", "prod"]