# Huawei LTE Band & Monitoring

Set band, show signal level and bandwidth for Huawei mobile broadband router B525s-23a. 
This program relies on an API provided by Salamek/huawei-lte-api

## Requirements
* python 3
* curses
* huawei-lte-api

## Installation
```sh
git clone git@github.com:octave21/huawei-lte.git
cd huawei-lte
pip install -r requirements.txt
chmod u+x lte.py
```

## Launch
```sh
./lte.py ip password stat|800|1800|2100|2600
```

## Examples
```sh
./lte.py 192.168.8.1 myPassword 800+2100
./lte.py 192.168.8.1 myPassword stat
```
