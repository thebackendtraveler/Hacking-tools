import pyfiglet
import sys
import socket
from datetime import datetime
import threading

ascii_banner = pyfiglet.figlet_format("RACCOON MAPPER")
print(ascii_banner)

target = input(str("target IP: "))

#Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:

    #Scan every port on the target ip
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        t = threading.Thread(target = (), args = ())
        t.setDaemon(True)
        t.start()

        #Return open port
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
except KeyboardInterrupt: 
        print("\n Exiting :(")
        sys.exit()
except socket.error:
        print("\n Host is not responding :(")
        sys.exit()