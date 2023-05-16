import scapy.all as scapy
import re 
from termcolor import cprint
import nmap


# The re module is used for creating regular expressions with scanners for example
# cprint is a function from the termcolor module, that allows us to change the color of the text in the terminal
# We use the scapy module for packet manipulation, for example in a network scanner
# We import the nmap module to be able to scan ports on a network

# The user interface header with the name of the tool, and a color guide
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



# Here is a try and except statement. We use them to help the program except errors and continue gracefully without crashing
#try:
    # Here we use regular expression to ensure the program will handle and reconize the ipv4 address, from user input
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
nmScan = nmap.PortScanner()     
    # Asking the user for a subnet to scan
ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        
    # This is an if statement that will search for the ip address range submitted by the user
    # If it existis, the scan will begin
    # If it does not exist, the program will display that soemthing went wrong, and then close
if ip_add_range_pattern.search(ip_add_range_entered):
    cprint(f"{ip_add_range_entered} is a valid ip address range", 'green') # This line will display when the user has provided a correct ip address range
    arp_result = scapy.arping(ip_add_range_entered) #This line will display the result of the scan to the user
    cprint(arp_result, 'green')
#except:
    #cprint(f'\n* Something went wrong, please try again  *', 'red')


nmScan.scan = ('192.168.142.132', '21 - 443')

#try:
for host in nmScan.all_hosts():
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
for proto in nmScan[host].all_protocols():
    print('----------')
    print('Protocol : %s' % proto)
 
lport = nmScan[host][proto].keys()
for port in lport:
    print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
#except:
    #cprint(f'\nThere was an error happening, please try again..', 'red')