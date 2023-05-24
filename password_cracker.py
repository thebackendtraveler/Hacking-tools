from termcolor import cprint
import hashlib
from urllib.request import urlopen
from datetime import datetime

# The password cracker starts
# User interface
cprint(
r"""
  _____    ______   _____   _____   _____   _____   ___     _      ____    _____   _____    ______   _____   _   _   ____   _____   
 |  _  \  |  __  | |  _  | |  _  | |  _  | |  _  | |   \   | |    |  _ \  |  _  | |  _  \  |  __  | |  _  | | | / / | ___| |  _  \  
 | | | |  | |  | | | | |_| | | |_| | | | | | | | | | |\ \  | |    | |_| | | | |_| | | | |  | |  | | | | |_| | |/ /  | |_   | | | |  
 | |_| /  | |__| | | |  _  | |  _  | | | | | | | | | | \ \ | | -> | ___/  | |  _  | |_| /  | |__| | | |     |    |  |  _|  | |_| /  
 |  __ \  |  __  | | |_| | | |_| | | |_| | | |_| | | |  \ \| |    | |     | |_| | |  __ \  |  __  | | |_| | | |\ \  | |__  |  __ \  
 |_|  \_\ |_|  |_| |_____| |_____| |_____| |_____| |_|   \___|    |_|     |_____| |_|  \_\ |_|  |_| |_____| |_| \_\ |____| |_|  \_\ 
                                                                                                                                     """, 'blue')


hash = input("Give me a hash to crack: ")

cprint("_" * 50, 'blue')
cprint("Cracking password " + hash, 'blue')
cprint("Password cracking started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

def crackHash(inputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find file")
    try:    
        for password in passFile:
            encPass = password.encode("utf-8")
            digest = hashlib.md5(encPass.strip()).hexdigest()
            if digest != inputPass:
                cprint("FAIL!! Wrong combination: " + password, 'red')
            if digest == inputPass:
                cprint("SUCCESS!! Password Found: " + password, 'green')
    except AttributeError:
        cprint('That is not the correct attribute. Please try again....', 'red')

if __name__ == '__main__':
    crackHash("d3eb05a3d5bb7e4901f739286ba8eee9")
    

        
