from termcolor import cprint
import hashlib
import pyfiglet
from datetime import datetime

# The password cracker starts
# User interface
banner = pyfiglet.figlet_format("RACCOON -> PCRACKER")
cprint(banner, 'blue')


#Asking the user for a string to hash, this will be checked towards the wordlists
hash = input("Enter a string to hash: ")

#The banner with information about when the cracking starts + the hash to be cracked
cprint("_" * 50, 'blue')
cprint("Cracking password " + hash, 'blue')
cprint("Password cracking started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')


def crackHash(digest2):
    """
    This function will hash the user input, 
    open the wordlist.txt and hash the passwords, 
    and compare it to the user input hash.
    """
    try:
        passFile = open("wordlist.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
    try:    
        for password in passFile:
            encHash = hash.encode("utf-8") # This line hashes the input string
            digest2 = hashlib.md5(encHash.strip()).hexdigest() # Here a digest for the input string is created
            cprint("Input hash: " + digest2, 'white')
            encPass = password.encode("utf-8") # This code is hashing the plain text passwords
            digest = hashlib.md5(encPass.strip()).hexdigest() # We are using the md5 hashing algorithm
            cprint("List hash : " + digest, 'white')
            if digest != digest2:
                # This code will only run when the digest is not the same as the crackHash
                cprint("FAIL!! Wrong combination: " + password, 'red')
            if digest == digest2:
                # This code runs when the digest is the same as crackHash
                cprint("SUCCESS!! Password Found: " + password, 'green')
    except:
        cprint('OOOPS, there was an error. Please try again...', 'red')

# This line is calling the crackHash function. The code will not run if this is removed.
if __name__ == '__main__':
    crackHash("d3eb05a3d5bb7e4901f739286ba8eee9")
    

        
