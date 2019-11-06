# huawei-lte
Huawei LTE Band & Monitoring

Set band, show signal level and bandwidth for Huawei mobile broadband B525s-23a. 
This program relies on API provided by Salamek/huawei-lte-api

REQUIREMENTS
python 3
curses
pip
git
huawei-lte-api

INSTALLATION
git clone git@github.com:octave21/huawei-lte.git
cd huawei-lte
pip install -r requirements.txt
chmod u+x lte.py

LAUNCH
./lte.py ip password stat|800|1800|2100|2600

Examples
./lte.py 192.168.8.1 myPassword 800+2100
./lte.py 192.168.8.1 myPassword stat


