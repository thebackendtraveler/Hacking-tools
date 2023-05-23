from termcolor import cprint
import hashlib
from urllib.request import urlopen
from datetime import datetime

# Basic user interface header
cprint(
r"""
  _____    ______   _____   _____   _____   _____   ___     _      ____    _____   _____    ______   _____   _   _   ____   _____   
 |  _  \  |  __  | |  _  | |  _  | |  _  | |  _  | |   \   | |    |  _ \  |  _  | |  _  \  |  __  | |  _  | | | / / | ___| |  _  \  
 | | | |  | |  | | | | |_| | | |_| | | | | | | | | | |\ \  | |    | |_| | | | |_| | | | |  | |  | | | | |_| | |/ /  | |_   | | | |  
 | |_| /  | |__| | | |  _  | |  _  | | | | | | | | | | \ \ | | -> | ___/  | |  _  | |_| /  | |__| | | |     |    |  |  _|  | |_| /  
 |  __ \  |  __  | | |_| | | |_| | | |_| | | |_| | | |  \ \| |    | |     | |_| | |  __ \  |  __  | | |_| | | |\ \  | |__  |  __ \  
 |_|  \_\ |_|  |_| |_____| |_____| |_____| |_____| |_|   \___|    |_|     |_____| |_|  \_\ |_|  |_| |_____| |_| \_\ |____| |_|  \_\ 
                                                                                                                                     """, 'blue')


url = "www.yourlinkgoeshere.com"
actual_password = "tomi"
actual_password_hash = "3675886jghjsnck9sjdkg"


cprint("_" * 50, 'green')
cprint("Cracking password " + actual_password_hash, 'green')
cprint("Password cracking started at: " + str(datetime.now()), 'green')
cprint("_" * 50, 'green')

def readwordlist(url):
    try:
        wordlistfile = urlopen(url)
    except: 
        cprint('There was an error while reading the wordlist..', 'red')
        exit()
    return wordlistfile

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            cprint('Hey!, your password is:', guess_password, "\n Please change this, it was easy to guess it :)", 'green')
        # If the password is found then it will terminate the script here
        exit()

wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('7n')
        
#Running the bruteforce attack 
bruteforce(guesspasswordlist, actual_password_hash)
#It would be executed if your password was not there in your wordlist
print('Hey, I could not find your password in the list, and I could not crack your password. Good job')
# Banner with information about the target, when the scan started