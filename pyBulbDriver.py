import os, time, subprocess, signal,re

mac = None
isConnected = False

def scanForBulb(devicename):
	global mac
	dev = subprocess.Popen(('hcitool lescan').split(), stdout = subprocess.PIPE)
	time.sleep(3)
	os.kill(dev.pid, signal.SIGINT)
	(device, err) = dev.communicate()

	for line in device.split('\n'):
		if(devicename in line):
			mac = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', 
			line, re.I).group()
			global isConnected
			isConnected = True
			print "found!"
			break;

def checksRGBInBounds(s,r,g,b):
        if((s >= 0 and s <= 255) and (r >= 0 and r <= 255) and (g >= 0 and g <= 255) and (b >= 0 and b <= 255)):
                return True
        return False

def checkModeAndSpeed(mode,offbeat,onbeat):
        if((mode > 0 and mode < 4) and (offbeat >= 1 and offbeat<=15) and (onbeat >= 1 and onbeat <= 15)):
                return True
        return False

def convertIntToHex(number):
	hexa = ""
	x = hex(number)
	xx = x.split('x');
	if len(str(xx[1])) < 2:
		hexa = '0'+str(xx[1])
	else:
		hexa = str(xx[1])
	return hexa

def convertRGBToHexaCmd(s,r,g,b):
        sRGB = convertIntToHex(s)+convertIntToHex(r)+convertIntToHex(g)+convertIntToHex(b)
        return sRGB        

def setBulbColor(s,r,g,b):
	global mac,isConnected
	checkSyntax = checksRGBInBounds(s,r,g,b)
	if isConnected and checkSyntax :
		cmd = convertRGBToHexaCmd(s,r,g,b)
		print cmd, mac
		subprocess.call(('gatttool -b '+mac+' --char-write -a 0x018 -n '+cmd).split())
	else:
                print "invalid command"

def setBulbEffect(s,r,g,b,mode,onbeat,offbeat):
	global mac,isConnected
	checkSyntax = checksRGBInBounds(s,r,g,b) & checkModeAndSpeed(mode,offbeat,onbeat)
	if isConnected and checkSyntax:
                sRGB = convertRGBToHexaCmd(s,r,g,b)
                hmode = convertIntToHex(mode)
                honbeat = convertIntToHex(onbeat)
                hoffbeat = convertIntToHex(offbeat)
                cmd = sRGB+hmode+"00"+honbeat+hoffbeat
		print cmd, mac
		subprocess.Popen(('gatttool -b '+mac+' --char-write -a 0x016 -n '+cmd).split(), stdout = subprocess.PIPE)
        else:
                print "invalid command"
