#!/usr/bin/python
#-*- coding: utf-8 -*-
# https://github.com/Salamek/huawei-lte-api

version = "6 novembre 2019"

#pdb.set_trace() # TRACE
import sys, pdb, os, base64, time, locale, traceback, curses 
from threading import Thread
from os.path import basename
from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

# Thread wait for keyboard press
class Keyboard(Thread) :
	"""Thread Keyboard"""
	def __init__(self) :
		"""Initialisation"""
		Thread.__init__(self)
	def run(self):
		"""Running thread code."""
		stdscr = curses.initscr()
		s = stdscr.getstr(11,0,1) # Wait for keyboard press
		stop = True

# Thread statistics loop
class Stat(Thread) :
	"""Thread Stat"""
	def __init__(self) :
		"""Initialisation"""
		Thread.__init__(self)
	def run(self):
		"""Running thread code."""
		stdscr = curses.initscr()
		curses.start_color()
		curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
		win = curses.newwin(20, 120, 0, 0)
		win.scrollok(1)
		bar = "##################################################################################"
		while not stop :
			bandRead = str(client.net.net_mode()["LTEBand"])
			if band == -2 :
				bandPrint = bandRead
			else :
				bandPrint = ""
				for bandl in bandsList :
					if bool(int(bandRead, 16) & int(bandl[3],16)) :
						bandPrint = bandPrint + bandl[1] + "-" + bandl[2] + " "
			#print("Band = " + bandPrint + "Mhz, Download : " + str(int(client.monitoring.traffic_statistics()['CurrentDownloadRate'])*8//1000000) + " Mbit/s, Upload : " + str(int(client.monitoring.traffic_statistics()['CurrentUploadRate'])*8//1000000) + " Mbit/s, rsrp = " + str(client.device.signal()["rsrp"]) + ", rsrq = " + str(client.device.signal()["rsrq"]) + ", sinr = " + str(client.device.signal()["sinr"]))
			download = int(client.monitoring.traffic_statistics()['CurrentDownloadRate'])*8//1000000
			upload = int(client.monitoring.traffic_statistics()['CurrentUploadRate'])*8//1000000
			rsrp = client.device.signal()["rsrp"]
			rsrq = client.device.signal()["rsrq"]
			sinr = client.device.signal()["sinr"]
			y = 1
			win.erase()
			win.addstr(y, 1, date + " - " + basename(sys.argv[0]))
			y += 2
			win.addstr(y, 1, "Band = " + bandPrint + "Mhz")
			y += 2
			win.addstr(y, 1, "Download : " + str(download) + "Mbit/s")
			win.addstr(y, 25, bar[0 : download % 50]) # Progress bar
			y += 1
			win.addstr(y, 1, "Upload :   " + str(upload) + "Mbit/s")
			win.addstr(y, 25, bar[0 : upload % 50]) # Progress bar
			y += 2
			win.addstr(y, 1, "rsrp = " + str(rsrp))
			y += 1
			win.addstr(y, 1, "rsrq = " + str(rsrq))
			y += 1
			win.addstr(y, 1, "sinr = " + str(sinr))
			y += 2
			win.addstr(y, 1, "Press enter to quit")
			y += 1
			win.addstr(y, 1, "")
			win.refresh()
			time.sleep(1)
		curses.endwin()

# Main program
# Global variables
stop = False
rep = "OK"
usage = "ip password stat|800|1800|2100|2600"
bandsList = [
    ('b1', 'FDD', '2100', '1'),
    ('b2', 'FDD', '1900', '2'),
    ('b3', 'FDD', '1800', '4'),
    ('b4', 'FDD', '1700', '8'),
    ('b5', 'FDD', '850', '10'),
    ('b6', 'FDD', '800', '20'),
    ('b7', 'FDD', '2600', '40'),
    ('b8', 'FDD', '900', '80'),
    ('b19', 'FDD', '850', '40000'),
    ('b20', 'FDD', '800', '80000'),
    ('b26', 'FDD', '850', '2000000'),
    ('b28', 'FDD', '700', '8000000'),
    ('b32', 'FDD', '1500', '80000000'),
    ('b38', 'TDD', '2600', '2000000000'),
    ('b40', 'TDD', '2300', '8000000000'),
    ('b41', 'TDD', '2500', '10000000000'),
]

# Input parameters
if (len(sys.argv) != 4) :
		print("Usage : " + basename(sys.argv[0]) + " " + usage)
		print("Examples :")
		print("lte.py 192.168.8.1 myPassword 800+2100")
		print("lte.py 192.168.8.1 myPassword stat")
		rep = "KO"
		exit()
ip = sys.argv[1]
password = sys.argv[2]
bandIn = sys.argv[3]

# Date & Version   
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8') # Heure Française
date = time.strftime('%d %B %Y - %H:%M:%S',time.localtime())
#print(date + " - " + basename(sys.argv[0]) + " : version du %s" %version)

# Service
if bandIn == "stat" :
	band = -1 # Monitoring only, no band set
elif bandIn == "manual" :
	band = -2 
	lteband = "80000" # Manual choice
else :
	bandTab = (bandIn.replace("+", " ")).split()
	band = 0
	for bandt in bandTab :
		if bandt == "800" :
			exp = int(bandsList[9][0].replace('b', ''))
		elif bandt == "1800" :
			exp = int(bandsList[2][0].replace('b', '')) 
		elif bandt == "2100" :
			exp = int(bandsList[0][0].replace('b', ''))
		elif bandt == "2600" :
			exp = int(bandsList[6][0].replace('b', '')) 
		else :
			rep = "KO"
			print("Unknown frequency")
			print("Usage : " + basename(sys.argv[0]) + " " + usage)
			exit()	
		band = band + 2**(exp-1)
	lteband =str(hex(band)).replace("0x", "")

# Set band
try :
	url = "http://admin:" + password + "@" + ip
	connection = AuthorizedConnection(url)
	client = Client(connection)
	networkband = "3FFFFFFF"
	networkmode = "03"
	if band != -1 :
		client.net.set_net_mode(lteband, networkband, networkmode) 
except Exception :
	print("Connexion error")
	exit()

# Statistics loop
keyboardThread = Keyboard() # Threads init
statThread = Stat()
keyboardThread.start() # Threads start
statThread.start()
keyboardThread.join() # wait for thread to stop
stop = True
statThread.join() # wait for thread to stop
exit()
