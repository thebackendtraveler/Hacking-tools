

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
subnet = input(str("Target subnet: " + subnet), 'green')


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
except scapy.error:
        cprint("\n Network is not responding :(", 'red')
        sys.exit()


