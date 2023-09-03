FROM alpine:latest
LABEL authors="Sergey Bobrov"
COPY . .
RUN apk add --update python3 py3-pip \
    && pip install -r requirements.txt \
    && pip install .