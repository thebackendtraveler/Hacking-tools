#!/usr/bin/env python3
# Import scapy
import scapy.all as scapy
# We need to create regular expressions to ensure that the input is correctly formatted.
import re
from termcolor import cprint

# Basic user interface header
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

# Get the address range to ARP
while True:
    ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        cprint(f"{ip_add_range_entered} is a valid ip address range", 'green')
        break