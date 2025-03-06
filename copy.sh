#!/usr/bin/env sh

set -e

mkdir -p ~/src/fonts
sudo cp ./Variants/FantasqueSansMono-*.zip ~/src/fonts/
sudo chown -R $(whoami) ~/src/fonts/FantasqueSansMono-*.zip
