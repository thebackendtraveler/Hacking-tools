import pyfiglet
import sys
import socket
from datetime import datetime
import threading
from termcolor import cprint

ascii_banner = pyfiglet.figlet_format("RACCOON MAPPER")
cprint(ascii_banner, 'blue')

target = input(str("target IP: "))

#Banner
cprint("_" * 50, 'green')
cprint("Scanning Target: " + target, 'green')
cprint("Scanning started at: " + str(datetime.now()), 'green')
cprint("_" * 50, 'green')

try:

    #Scan every port on the target ip
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open port
        result = s.connect_ex((target, port))
        if result == 0:
            cprint("[*] Port {} is open".format(port), 'green')
        s.close()
except KeyboardInterrupt: 
        cprint("\n Exiting :(", 'red')
        sys.exit()
except socket.error:
        cprint("\n Host is not responding :(", 'red')
        sys.exit()