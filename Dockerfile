FROM ubuntu:24.04

RUN set -eux; \
    apt-get dist-clean; \
    apt-get update; \
    apt-get dist-upgrade -y; \
    apt-get autoremove -y; \
    apt-get install -y --no-install-recommends \
        fontforge \
        woff-tools \
        woff2 \
        ttfautohint \
        make \
        zip \
    ; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /fantasque

VOLUME /fantasque/Release

COPY . /fantasque

CMD ["make"]
