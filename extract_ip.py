import re
import sys

iface="Local Area Connection"


def extractIp(line):
	ipPat="\s*IPv4 Address[\. ]+: ([^\(]+)\(Preferred\)\s*"
	ipMatch=re.match(ipPat,line)
	if (ipMatch != None):
		ip=ipMatch.group(1)
	else:
		ip=None
	return(ip)

def extractMac(line):
	print("check mac address "+line)
	ipPat="\s*Physical Address[\. ]+: ([^\s]+)\s*"
	ipMatch=re.match(ipPat,line)
	if (ipMatch != None):
		ip=ipMatch.group(1)
	else:
		ip=None
	return(ip)

def extractFromFile(f):
	f=open(f)
	lines=f.readlines()
	ifaceFound=False
	extractedIp=""
	extractedMac=""
	ifaceFound=0
	for line in lines:
		if (ifaceFound==0):
			if (re.search(".*"+iface+":\s*",line) != None):
				ifaceFound=1
		elif (ifaceFound==1):
			ip=extractIp(line)
			if (ip != None):
				extractedIp = ip
			else:
				mac=extractMac(line)
				if (mac != None):
					extractedMac=mac 
				else:
					if (re.match("[^\s].*:\s*",line) != None):
						ifaceFound=2
	print(extractedIp,extractedMac)



files=sys.argv[1:]

for file in files:
	extractFromFile(file)