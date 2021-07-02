#!/usr/bin/env sh

sudo make clean
docker build -t fantasque .
docker run -v "$(pwd)/Variants:/fantasque/Variants" fantasque
