__author__ = 'bcoates'

import socket
import subprocess
import sys
import os
from datetime import datetime

common_dict = {'FTP':21, 'SSH':22, 'Telnet':23, 'SMTP':25,
             'internet':80,'SFTP':115,'altHTTP':8080}

#Clear the screen
if sys.platform =='linux' or sys.platform=='linux2' or sys.platform=='darwin':
    clearcommand = 'clear'
else:
    clearcommand = 'cls'
os.system(clearcommand)

if len(sys.argv) != 3:
    print "Usage: python PortScanner.py <targetIP> <scantype>"
    sys.exit(1)

#Getting the arguments
scantype = sys.argv[2]
ipAddr = sys.argv[1]
targetIP= socket.gethostbyname(ipAddr)

if scantype == 'common' or scantype=='Common':
    print "About to perform a common scan on: " + ipAddr
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
