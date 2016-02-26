#!/usr/bin/python
import os
import sys,getopt
import csv
import socket

def main():
	inputfile = ''
	ip_list = []
	outputcsv = "output.csv"
	for i in range(0,len(sys.argv)):
		arg = sys.argv[i]
		if(arg == '-i'):
			inputfile = sys.argv[i+1]
		elif(arg == '-h'):
			print("lookup.py -i <inputcsv>")
	hostnames = []
	with open(inputfile) as csvfile:
		reader = csv.reader(csvfile, dialect = 'excel')
		for column in reader:
			hostnames.append(column[1])
	print("You have " + str(len(hostnames) - 1 ) + " hostnames")
	hostnames[0] = hostnames[1]

	for i in range(0, len(hostnames)):
		try:
			ais = socket.getaddrinfo(hostnames[i],0,0,0,0)
			ip_list.append(ais[-1][4][0])
		except socket.gaierror:
			ip_list.append("error")
			print(socket.gaierror)
		
		print(ais[-1][4][0])

	with open(str(outputcsv), 'w') as f:
		f.write("nslookupIP,\n")
		f.write(ip_list[0] + ',\n')
		for ip in ip_list:
			if(ip != ip_list[0]):
				f.write(ip + ',\n')
			else:
				pass
	
main()