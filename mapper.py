import sys
import socket
from datetime import datetime
from termcolor import cprint
import scapy.all as scapy
import re 

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

subnet_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
subnet_range_entered = input("\n Target subnet (ex 192.168.1.0/24): ")



#Banner
cprint("_" * 50, 'green')
cprint("Scanning Subnet " + subnet_range_entered, 'green')
cprint("Scanning started at: " + str(datetime.now()), 'green')
cprint("_" * 50, 'green')


try:
    #Scan every host on the target subnet
    if subnet_range_pattern.search(subnet_range_entered):
        cprint(f"{subnet_range_entered} is a valid ip address range", 'green')

        #Return ipaddresses from the subnet 
        arp_result = scapy.arping(subnet_range_entered)
        cprint(arp_result, 'green')
except KeyboardInterrupt:
        cprint("\n Exiting :(", 'red')
        sys.exit()
except TimeoutError:
        cprint("\n Network is not responding :(", 'red')
        sys.exit()


# The port scanner code starts

#Menu
cprint("_" * 50, 'green')
cprint("172.0.0.1: Localhost", 'green')
cprint("192.168.142.133: Localhost", 'green')
cprint("192.168.142.132: Windows PC", 'green')

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
except TimeoutError:
        cprint("\n Host is not responding :(", 'red')
        sys.exit()



#I want to be able to select ip addresses from the ones scapy uncovered. So much like a menu program
#when the user selects ip address one, this should be scanned for open ports.

