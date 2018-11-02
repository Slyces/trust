#/usr/bin/env bash

dir=$(pwd)

# On part du principe que ton unix est en français
cd ~/Téléchargements
rm -rf MOSIMA*

# Attention: avoir overleaf ouvert
firefox https://www.overleaf.com/project/5bd1cdac9f3f0040d146275f/download/zip

sleep 1

unzip -q -o MOSIMA.zip -d $dir/rapport
cd - > /dev/null
