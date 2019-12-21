# Huawei LTE Band & Monitoring

For Huawei mobile broadband router B525s-23a, set band, show signal level and bandwidth, show monthly traffic. 
This program relies on an API provided by [Salamalek](https://github.com/Salamek/huawei-lte-api)

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
./lte.py ip password stat|700|800|1800|2100|2600
```

## Examples
```sh
./lte.py 192.168.8.1 myPassword stat
./lte.py 192.168.8.1 myPassword 800+2100
./lte.py 192.168.8.1 myPassword 800
```
![lte](/lte.png)
![Bandes](/tableau_bandes-frequences-mobiles.png)
