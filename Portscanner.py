#!/bin/python3
#Vickyarts Github
#Contact me on github

import sys
import socket
from datetime import datetime

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
Y = '\033[33m' # yellow

if len(sys.argv) == 4:
       target = socket.gethostbyname(sys.argv[1])
       stport = sys.argv[2]
       edport = sys.argv[3]

elif len(sys.argv) == 3:
       target = socket.gethostbyname(sys.argv[1])
       stport = sys.argv[2]
       edport = sys.argv[2]

elif len(sys.argv) == 2:
       target = socket.gethostbyname(sys.argv[1])
       stport = 1
       edport = 65535

elif len(sys.argv) > 4 or len(sys.argv) < 2:
        print(C + "Usage:")
        print(Y + "For single port scan:-")
        print(W + "python3 scanner.py <ip> <port>")
        print(Y + "For multiple port scan:-")
        print(W + "python3 scanner.py <ip> <from> <to>")
        print(Y + "To scan all the ports:-")
        print(W + "python3 scanner.py <ip>")
        print(Y + "Only to show open ports:-")
        print(W + "python3 scanner.py <ip> <from> <to> | grep \"open\"\n")
        sys.exit()
else:
        sys.exit()

#Pretty banner
print(W + "-" * 50)
print(Y + "Scanning target:" + target)
print(Y + "Time started: " + str(datetime.now()))
print(W + "-" * 50)
print(C + "Checking ports:")
try:
          for port in range(int(stport),int(edport) + 1):
                  s = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
                  socket.setdefaulttimeout(1)
                  result = s.connect_ex((target,port))
                  if result == 0:
                          print(G + "[+]Port {} is open ".format(port))
                          s.close()
                  else:
                          print(R + "[-]Port {} is closed".format(port))
                          s.close()
except KeyboardInterrupt:
                  print("\nExiting program.")
                  sys.exit()

except socket.gaierror:
                  print("Hostname could not be resolved.")
                  sys.exit()

except socket.error:
                  print("Couldn't connect to server.")
                  sys.exit()

