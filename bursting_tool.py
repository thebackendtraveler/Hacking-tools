from termcolor import cprint
import pyfiglet
import sys
import socket
import requests

rhost = input("Which remote host is your target? ")
wordlist = input("What file do you want to use? ")

# Basic user interface header
banner = pyfiglet.figlet_format("RACCOON -> BURSTER")
cprint(banner, 'blue')

# This is the code that will check the RHOST to see if it is valid
cprint("[*] Checking RHOST.....", 'green')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    status = s.connect_ex((rhost, 80))
    s.close()
    if status == 0:
        cprint("[*] DONE", 'green')
        pass
    else:
        cprint("[*] FAIl; There was an error...", 'red')
        sys.exit(1)
except socket.error:
    cprint("[*] Cannot reach RHOST: %s\n")
    sys.exit(1)

# This is the code that will check the wordlist file for relevant words to use
cprint("[*] Checking wordlist...", 'green')
try:
    with open(wordlist) as file:
            to_check = file.read().strip().split('\n')
    cprint("[*] Success! Done", 'green')
    cprint("[*] Total paths to check: %s" %(str(len(to_check))))
except IOError: 
     cprint("[*] Failed to read the specified file...", 'red')
     sys.exit()

# This is the core of the directory bursting. It will check for valid paths compared with the wordlist
def checkpath(path):
    try:
        response = requests.get('http://' + rhost + '/' + path).status_code
        if response == 200:
                cprint("[*] Valid path found: /%s", 'green')
                cprint("\n[*] Beginning scan...\n", 'green')
                for i in range(len(to_check)):
                        checkpath(to_check[i])
                cprint("[*] Success! Scan Complete!", 'green')

    except KeyboardInterrupt:
            cprint("[*] An error happened. The user inerrupted the scan")
            sys.exit(1)
    except Exception:
         cprint("[*] An unexpefcted error occurred..")