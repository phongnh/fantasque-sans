#!/usr/bin/env sh

sudo make clean
mkdir -p Variants
docker build -t fantasque .
docker run --rm -v "$(pwd)/Variants:/fantasque/Variants" fantasque
