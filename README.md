# Huawei LTE Band & Monitoring

For Huawei mobile broadband router B525s-23a, set band, show signal level and bandwidth, show monthly traffic. 
This program relies on an API provided by [Salamek](https://github.com/Salamek/huawei-lte-api)

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

## Run
```sh
./lte.py ip password stat|700|800|1800|2100|2300|2600 [ping url]
```

## Examples
```sh
python lte.py 192.168.8.1 myPassword stat
python lte.py 192.168.8.1 myPassword 800+2100
python lte.py 192.168.8.1 myPassword 800
python lte.py 192.168.8.1 myPassword stat https://github.com
```
![lte](/lte.png)
![Bandes](/tableau_bandes-frequences-mobiles.png)

## Ping http
Shell script which measures the http response time and traces the results in the tracemn.log file.
* Measurements are spaced one second apart
* There are 60 measures
* Recording in the log file of the average response times of the 60 measurements
```sh
./ping.sh url
```
