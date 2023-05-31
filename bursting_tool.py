from termcolor import cprint
import pyfiglet
import sys
import socket
import requests
from datetime import datetime

try:
    rhost = input("Which remote host is your target? (ex. 192.168.142.138): ")
    wordlist = input("What file do you want to use? (ex wordfile.txt): ")

    # Basic user interface header
    banner = pyfiglet.figlet_format("RACCOON -> BURSTER")
    cprint(banner, 'blue')

    #The banner with information about when the cracking starts + the hash to be cracked
    cprint("_" * 50, 'blue')
    cprint("Remote host is " + rhost, 'blue')
    cprint("Wordfile is " + wordlist, 'blue')
    cprint("Directory bursting started at: " + str(datetime.now()), 'blue')
    cprint("_" * 50, 'blue')

    # This is the code that will check the RHOST to see if it is valid
    cprint("[*] Checking RHOST.....[Done]", 'green')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        status = s.connect_ex((rhost, 80))
        s.close()
        if status == 0:
            cprint("[*] DONE checking RHOST", 'green')
            pass
        else:
            cprint("[*] Attempt unsuccessful. There was an error...", 'red')
            sys.exit(1)
    except socket.error:
        cprint("[*] Cannot reach RHOST: %s", 'red')
        sys.exit(1)

    # This is the code that will check the wordlist file for relevant words to use
    cprint("[*] Checking wordlist...[Done]", 'green')
    try:
        with open(wordlist) as file:
                to_check = file.read().strip().split('\n')
        cprint("[*] DONE checking wordlist", 'green')
        cprint("[*] Total paths to check: %s" %(str(len(to_check))), 'green')
    except IOError: 
        cprint("[*] Failed to read the specified file...", 'red')
        sys.exit()

    print('This works 1')
    # This is the core of the directory bursting. It will check for valid paths compared with the wordlist
    def checkpath(path):
            
            try:
                    print('This works 2')
                    response = requests.get('http://' + rhost + '/' + path).status_code
            except Exception:
                    cprint("[*] An unexpefcted error occurred..", 'red')
                    
            if response != 200:
                    print("Ooops the response code is not 200")
            if response == 200:
                    cprint("[*] Valid path found: /%s", 'green')
                    cprint("[*] Beginning scan...", 'green')
                    for i in range(len(to_check)):
                            checkpath(to_check[i])
                    cprint("[*] Success! Scan Complete!", 'green')

except KeyboardInterrupt:
        cprint("[*] An error happened. The user inerrupted the scan", 'red')
        sys.exit(1)
