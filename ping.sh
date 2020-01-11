#! /bin/sh
# 10 janvier 2020

if [ $# -ne 1 ] ; then
	echo " "
	echo "usage $0 url"
	exit 1
fi

PAGE=$HOME"/accueil.html"
nb=1 # Boucle sans fin
while ((nb!=0))
do
	# Calcul de la moyenne des "nbMesures" effectuées
	nbMesures=60 
	i=0
	cumul=0
	dateStart="$(date  "+%A %d %B %Y %H:%M:%S")"
	timeStart="$(date +%s%N)"
	while ((i<nbMesures))
	do
		echo -n "*"
		t1="$(date +%s%N)"
		curl -s -o $PAGE --insecure $1
		t2="$((($(date +%s%N)-t1)/1000000))" # Temps du ping
		#echo "Ping unitaire "$i" "$t2" ms"
		cumul=$((cumul + t2))
		sleep 1 
		i=$((i+1))
	done
	moyenne=$((cumul/nbMesures))
	print=$moyenne" ms - "$dateStart" - "$1" - "$timeStart
	echo -e "\r"$print
	echo $print >> tracemn.log
done	
