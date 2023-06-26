#!/bin/bash


pip3 install pyzabbix
cd data
python3 -m http.server 8080 &

cd /app
while true;
do
    python3 getall.py > data/lista.txt
    sleep 3600
done