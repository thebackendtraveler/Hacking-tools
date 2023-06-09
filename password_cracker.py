from termcolor import cprint
import hashlib
import pyfiglet
from datetime import datetime

# The password cracker starts
# User interface
banner = pyfiglet.figlet_format("RACCOON -> PCRACKER")
cprint(banner, 'blue')


#Asking the user for a string to hash, this will be checked towards the wordlists
# For this tool the wordlist is called wordlist.txt
hash = input("Enter a password to hash: ")
wordlist = input("Enter a wordlist you want to use: ")


#The banner with information about when the cracking starts + the hash to be cracked
cprint("_" * 50, 'blue')
cprint("Cracking password " + hash, 'blue')
cprint("The wordlist is: ", wordlist, 'blue')
cprint("Password cracking started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

print("\n")
cprint("MD5 cracking is starting...", 'green')
def crackHash_md5(inputHash):
    """
    This function will hash the user input, 
    open the wordlist.txt and hash the passwords, 
    and compare it to the user input hash.
    """
    try:
        passFile = open(wordlist, "r+").read()
        password = passFile.splitlines()

    except FileNotFoundError:
        print("Could not find file")
    try:    
        for password in passFile:
            encHash = hash.encode("utf-8") # This line hashes what the user inputed
            inputHash = hashlib.md5(encHash.strip()).hexdigest() # Here a digest for the input string is created
            cprint("Input hash: " + inputHash, 'white')
            encPass = password.encode("utf-8") # This code is hashing the plain text passwords
            wordlistHash = hashlib.md5(encPass.strip()).hexdigest() # We are using the md5 hashing algorithm
            cprint("List hash : " + wordlistHash, 'white')

            fdw = open("pcrack_results.txt", "+a")
            fdw.write("\n")
            fdw.write("MD5 hash: ")
            fdw.write(wordlistHash + '\n')

            if wordlistHash != inputHash:
                # This code will only run when the input hash is not the same as one of the wordlist hashes
                cprint("FAIL!! Wrong combination: " + password, 'red')
                
            if wordlistHash == inputHash:
                # This code runs when the input hash is the same as one of the wordlist hashes
                cprint("SUCCESS!! Password Found: " + password, 'green')
                
    except KeyboardInterrupt:
        cprint('Quitting! THe program was terminated by the user', 'red')
    except:
        cprint('OOOPS, there was an error. Please try again...', 'red')

# This line is calling the crackHash function. The code will not run if this is removed.
# The hash here acts as a placeholder, and ti makes sure the input is correct
if __name__ == '__main__':
    crackHash_md5("d3eb05a3d5bb7e4901f739286ba8eee9")

print("\n")
cprint("SHA256 cracking is starting...", 'green')
def crackHash_sha256(inputHash):
    """
    This function will hash the user input, 
    open the wordlist.txt and hash the passwords, 
    and compare it to the user input hash.
    It will use the sha256 algortihm.
    """
    try:
        passFile = open("wordlist.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
    try:    
        for password in passFile:
            encHash = hash.encode("utf-8") # This line hashes what the user inputed
            inputHash = hashlib.sha256(encHash.strip()).hexdigest() # Here a digest for the input string is created
            cprint("Input hash: " + inputHash, 'white')
            encPass = password.encode("utf-8") # This code is hashing the plain text passwords
            wordlistHash = hashlib.sha256(encPass.strip()).hexdigest() # We are using the md5 hashing algorithm
            cprint("List hash : " + wordlistHash, 'white')

            fdw = open("pcrack_results.txt", "+a")
            fdw.write("\n")
            fdw.write("SHA256 hash: ")
            fdw.write(wordlistHash + '\n')
            if wordlistHash != inputHash:
                # This code will only run when the input hash is not the same as one of the wordlist hashes
                cprint("FAIL!! Wrong combination: " + password, 'red')
    
            if wordlistHash == inputHash:
                # This code runs when the input hash is the same as one of the wordlist hashes
                cprint("SUCCESS!! Password Found: " + password, 'green')
                
    except KeyboardInterrupt:
        cprint('Quitting! THe program was terminated by the user', 'red')
    except:
        cprint('OOOPS, there was an error. Please try again...', 'red')

# This line is calling the crackHash function. The code will not run if this is removed.
# The hash here is a placeholder, and it makes sure the input is a 256 hash
if __name__ == '__main__':
    crackHash_sha256("da088df0c22020eda7fef865007b2465bd6ed0fb8a47bdf10a75470ecca4559d")


print("\n")
cprint("SHA512 cracking is starting...", 'green')
def crackHash_sha512(inputHash):
    """
    This function will hash the user input, 
    open the wordlist.txt and hash the passwords, 
    and compare it to the user input hash. 
    It will use the sha512 algorithm.
    """
    try:
        passFile = open("wordlist.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
    try:    
        for password in passFile:
            encHash = hash.encode("utf-8") # This line hashes what the user inputed
            inputHash = hashlib.sha512(encHash.strip()).hexdigest() # Here a digest for the input string is created
            cprint("Input hash: " + inputHash, 'white')
            encPass = password.encode("utf-8") # This code is hashing the plain text passwords
            wordlistHash = hashlib.sha512(encPass.strip()).hexdigest() # We are using the md5 hashing algorithm
            cprint("List hash : " + wordlistHash, 'white')

            fdw = open("pcrack_results.txt", "+a")
            fdw.write("\n")
            fdw.write("SHA 512 hash: ")
            fdw.write(wordlistHash + '\n')
    
            if wordlistHash != inputHash:
                # This code will only run when the input hash is not the same as one of the wordlist hashes
                cprint("FAIL!! Wrong combination: " + password, 'red')
            if wordlistHash == inputHash:
                # This code runs when the input hash is the same as one of the wordlist hashes
                cprint("SUCCESS!! Password Found: " + password, 'green')
              
                                       
    except FileNotFoundError:
        print("Sorry, the file does not exist...", 'red')
    except FileExistsError:
        print("Cannot create a new file, because it already exists..", 'red')
    except KeyboardInterrupt:
        cprint('Quitting! THe program was terminated by the user', 'red')
    except:
        cprint('OOOPS, there was an error. Please try again...', 'red')


# This line is calling the crackHash function. The code will not run if this is removed.
# The hash here is a placeholder, and it makes sure the input for the program is a 512 hash
if __name__ == '__main__':
    crackHash_sha512("acb70dbd1969d70601892f3dd668919cfd2398fd440aaf8c6157620df352843ce5bd9d9dc3f167e6993b90a0d28f1015eb820e99a0625a2923376a71f4944925")


    
        
