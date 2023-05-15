#!/usr/bin/env python3

import scapy.all as scapy
import re #the re module is for regular expressions
from termcolor import cprint

# Basic user interface header with the name of the tool, and a color guide
cprint(
r""" ____________________________________________________________________________________________________________________________ 
|  _____    ______   _____   _____   _____   _____   ___     _      ___        ___   ______   _____   _____   ____   _____   |
| |  _  \  |  __  | |  _  | |  _  | |  _  | |  _  | |   \   | |    |   \      /   | |  __  | |  _  \ |  _  \ | ___| |  _  \  |
| | | | |  | |  | | | | |_| | | |_| | | | | | | | | | |\ \  | |    | |\ \    / /| | | |  | | | |_| | | |_| | | |__  | | | |  |
| | |_| |  | |__| | | |  _  | |  _  | | | | | | | | | | \ \ | | -> | | \ \  / / | | | |__| | |  ___/ |  ___/ |  __| | |_| |  | 
| |  __ \  |  __  | | |_| | | |_| | | |_| | | |_| | | |  \ \| |    | |  \ \/ /  | | |  __  | | |     | |     | |__  |  __ \  |
| |_|  \_\ |_|  |_| |_____| |_____| |_____| |_____| |_|   \___|    |_|   \__/   |_| |_|  |_| |_|     |_|     |____| |_|  \_\ |
|____________________________________________________________________________________________________________________________| """, 'blue')
cprint(f'\n************************************************', 'blue')
cprint(f'\n* Copyright of Andrea Dybendal, 2023           *', 'blue')
cprint(f'\n* https://www.thebackendtraveler.com           *', 'blue')
cprint(f'\n* https://www.youtube.com/thebackendtraveler   *', 'blue')
cprint(f'\n************************************************', 'blue')

cprint(f'\n* Color guide:                                *', 'white')
cprint(f'\n* Red -> There was an error.                  *', 'red')
cprint(F'\n* Green -> No error.                          *', 'green')

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

try:
    def network_mapper(ip_add_range_entered, arp_result) :
        ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        
        if ip_add_range_pattern.search(ip_add_range_entered):
            cprint(f"{ip_add_range_entered} is a valid ip address range", 'green')
            arp_result = scapy.arping(ip_add_range_entered)
            cprint(arp_result, 'green')
except:
    cprint(f'\n* Something went wrong, please try again  *', 'red')

    
