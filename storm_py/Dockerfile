FROM alpine:3.9

RUN apk add --no-cache python3-dev && \
    apk add --no-cache bash && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk --update add openjdk8-jre

ENV LEIN_ROOT=1
RUN wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \
    chmod +x lein && \
    mv lein /usr/local/bin 

RUN apk --update add libressl-dev libffi-dev

RUN apk --update add build-base
    
RUN pip3 install streamparse

RUN apk add openssh-client

RUN mkdir /root/.ssh && touch /root/.ssh/config

RUN pip install pykafka


