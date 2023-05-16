import pyfiglet
import sys
import socket
from datetime import datetime
import threading
from termcolor import cprint
import scapy.all as scapy
import re 

#User interface
cprint(
r""" ____________________________________________________________________________________________________________________________ 
|  _____    ______   _____   _____   _____   _____   ___     _      ___        ___   ______   _____   _____   ____   _____   |
| |  _  \  |  __  | |  _  | |  _  | |  _  | |  _  | |   \   | |    |   \      /   | |  __  | |  _  \ |  _  \ | ___| |  _  \  |
| | | | |  | |  | | | | |_| | | |_| | | | | | | | | | |\ \  | |    | |\ \    / /| | | |  | | | |_| | | |_| | | |__  | | | |  |
| | |_| |  | |__| | | |  _  | |  _  | | | | | | | | | | \ \ | | -> | | \ \  / / | | | |__| | |  ___/ |  ___/ |  __| | |_| |  | 
| |  __ \  |  __  | | |_| | | |_| | | |_| | | |_| | | |  \ \| |    | |  \ \/ /  | | |  __  | | |     | |     | |__  |  __ \  |
| |_|  \_\ |_|  |_| |_____| |_____| |_____| |_____| |_|   \___|    |_|   \__/   |_| |_|  |_| |_|     |_|     |____| |_|  \_\ |
|____________________________________________________________________________________________________________________________| """, 'blue')

subnet = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
subnet = input("Target subnet: " )



#Banner
cprint("_" * 50, 'green')
cprint("Scanning Subnet " + subnet, 'green')
cprint("Scanning started at: " + str(datetime.now()))
cprint("_" * 50, 'green')


try:
    #Scan every host on the target subnet
    if subnet.search(subnet):
        cprint(f"{subnet} is a valid ip address range", 'green')

        #Return ipaddresses from the subnet 
        arp_result = scapy.arping(subnet) 
        cprint(arp_result, 'green')
except KeyboardInterrupt:
        cprint("\n Exiting :(", 'red')
        sys.exit()
#except:
        #cprint("\n Network is not responding :(", 'red')
        #sys.exit()


#User interface
cprint(
r""" 
  _____    ______   _____   _____   _____   _____   ___     _      ___        ___   ______   _____   _____   ____   _____   
 |  _  \  |  __  | |  _  | |  _  | |  _  | |  _  | |   \   | |    |   \      /   | |  __  | |  _  \ |  _  \ | ___| |  _  \ 
 | | | |  | |  | | | | |_| | | |_| | | | | | | | | | |\ \  | |    | |\ \    / /| | | |  | | | |_| | | |_| | | |__  | | | |  
 | |_| |  | |__| | | |  _  | |  _  | | | | | | | | | | \ \ | | -> | | \ \  / / | | | |__| | |  ___/ |  ___/ |  __| | |_| |  
 |  __ \  |  __  | | |_| | | |_| | | |_| | | |_| | | |  \ \| |    | |  \ \/ /  | | |  __  | | |     | |     | |__  |  __ \  
 |_|  \_\ |_|  |_| |_____| |_____| |_____| |_____| |_|   \___|    |_|   \__/   |_| |_|  |_| |_|     |_|     |____| |_|  \_\ 
                                                                                                                             """, 'blue')

target = input(str("Target IP: "))

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