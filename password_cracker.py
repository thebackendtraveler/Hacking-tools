from termcolor import cprint
import hashlib
import pyfiglet
from datetime import datetime
import sys

# Basic user interface
banner = pyfiglet.figlet_format("RACCOON -> PCRACKER")
cprint(banner, 'blue')

#Asking the user for a wordlist
wordlist = input("Enter a wordlist to use: ")
try:
    def crackHash_md5(inputHash):
        """
            This function will hash the user input, 
            open the wordlist the user selected and hash the passwords.
            Next, it will compare the wordlist hashes to the user input hash.
            This function will use the MD5 algorithm.
        """
   
        #Asking the user for a  hash 
        inputHash = input("Enter a hash: ")
       
        #The banner with information about when the cracking starts + the hash to be cracked
        cprint("_" * 50, 'blue')
        cprint("Cracking hash: " + inputHash, 'blue')
        cprint("The wordlist is:  " + wordlist, 'blue')
        cprint("Cracking hashes started at: " + str(datetime.now()), 'blue')
        cprint("_" * 50, 'blue')

        print("\n") # Printing an empty line to make the output nicer
        cprint("MD5 cracking is starting...", 'green')

        passFile = open(wordlist, "r+")
        
        for password in passFile:
            #encHash = hash.encode("utf-8") # This line hashes what the user inputed
            #inputHash = hashlib.md5(encHash.strip()).hexdigest() # A digest for the input string is created
            encPass = password.encode("utf-8") # This code is hashing the wordlist passwords
            wordlistHash = hashlib.md5(encPass.strip()).hexdigest() # The program is using  md5 

            fdw = open("pcrack_results.txt", "+a") # Here the program is opening a file in +a mode
            fdw.write("\n")
            fdw.write("Valid MD5 hash: ") # Then the program writes the results of the cracking to the file
            fdw.write(wordlistHash + '\n')
            fdw.close() # Then the file is closed
     
            if wordlistHash == inputHash:
                # This code runs when the input hash is the same as one of the wordlist hashes
                 cprint("Input hash: " + inputHash, 'white')
                 cprint("List hash : " + wordlistHash, 'white')
                 cprint("SUCCESS!! Password Found :) : " + password, 'green')
            else: 
                 cprint("Input hash: " + inputHash, 'white')
                 cprint("List hash : " + wordlistHash, 'white')
                 cprint("FAIL!! Password Not Found :( : " + password, 'red')
                 # If the hashes are not the same, the program prints that to the user, and continues
                 pass
    
    # This line is calling the crackHash_md5 function. The code will not run if this is removed.
    # The hash here acts as a placeholder, and it makes sure the input is correct
    if __name__ == '__main__':
        crackHash_md5("")   
# Here is a complex exception statement that tells the program what to do when there is an error
except KeyboardInterrupt:
        cprint('Quitting! THe program was terminated by the user', 'red')
        sys.exit()
except FileNotFoundError:
        cprint("Could not find the specific file...", 'red')
        sys.exit()
except PermissionError: 
        cprint("WARNING! You are not root, and you have too little privileges...", 'red')
        sys.exit()
except FileExistsError:
        cprint("This file already exixts, try to write to another file..", 'red')
        sys.exit()
except ValueError: 
        cprint("That is not the correct value. Try again...", 'red')
        sys.exit()

print("\n")

try: 
    def crackHash_sha256(inputHash):
        """
            This function will hash the user input, 
            open the wordlist the user selected and hash the passwords. 
            Next, the program will compare the wordlist hash to the user input hash.
            This function will use the SHA256 algorithm. 
        """
        
        # Asking the user for a hash to compare with the wordlist
        inputHash = input("Enter a hash: ")
        passFile = open(wordlist, "r")
        print("\n")

        cprint("SHA256 cracking is starting...", 'green')
   
        for password in passFile:
            #encHash = hash.encode("utf-8") # This line hashes what the user inputed
            #inputHash = hashlib.sha256(encHash.strip()).hexdigest() # Here a digest for the input string is created
            encPass = password.encode("utf-8") # This code is hashing the plain text passwords
            wordlistHash = hashlib.sha256(encPass.strip()).hexdigest() # We are using the md5 hashing algorithm
        
            fdw = open("pcrack_results.txt", "+a") # Here the program is opening the output file in +a mode
            fdw.write("\n")
            fdw.write("Valid SHA256 hash: ")
            fdw.write(wordlistHash + '\n')
            fdw.close() # The file is closed by the program

            if wordlistHash == inputHash:
                 # This code runs when the input hash is the same as one of the wordlist hashes
                 cprint("Input hash: " + inputHash, 'white')
                 cprint("List hash : " + wordlistHash, 'white')
                 cprint("SUCCESS!! Password Found :) : " + password, 'green')
            else:
                 cprint("Input hash: " + inputHash, 'white')
                 cprint("List hash : " + wordlistHash, 'white')
                 cprint("FAIL!! Password Not Found :( : " + password, 'red')
                 # If the hashes are not the same, the program prints that to the user, and continues
                 pass
                
    # This line is calling the crackHash function. The code will not run if this is removed.
    # The hash here is a placeholder, and it makes sure the input is a 256 hash
    if __name__ == '__main__':
        crackHash_sha256("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
# Here the program has instructions for what to do when it encounters an error
except KeyboardInterrupt:
        cprint('Quitting! THe program was terminated by the user', 'red')
        sys.exit()
except FileNotFoundError:
        cprint("Could not find the file requested...", 'red')
        sys.exit()
except FileExistsError: 
        cprint("This file already exists. Try writing to another file...")
        sys.exit()

print("\n")

try: 
    def crackHash_sha512(inputHash):
        """
            This function will hash the user input, 
            open the wordlist.txt and hash the passwords, 
            and compare it to the user input hash. 
            This function will use the sha512 algorithm.
        """
        
        #Asking the user for a string to hash 
        inputHash = input("Enter a hash: ")
        passFile = open(wordlist, "r")
        print("\n")
        cprint("SHA512 cracking is starting...", 'green')

        for password in passFile:
            #encHash = hash.encode("utf-8") # This line hashes what the user inputed
            #inputHash = hashlib.sha512(encHash.strip()).hexdigest() # Here a digest for the input string is created
            
            encPass = password.encode("utf-8") # This code is hashing the plain text passwords
            wordlistHash = hashlib.sha512(encPass.strip()).hexdigest() # We are using the md5 hashing algorithm
            
            fdw = open("pcrack_results.txt", "+a") # The file is opened in +a to append more lines
            fdw.write("\n")
            fdw.write("Valid SHA 512 hash: ") # Then the program writes the results to a file
            fdw.write(wordlistHash + '\n')
    
            if wordlistHash == inputHash:
                 # This code runs when the input hash is the same as one of the wordlist hashes
                 cprint("Input hash: " + inputHash, 'white')
                 cprint("List hash : " + wordlistHash, 'white')
                 cprint("SUCCESS!! Password Found :) : " + password, 'green')
            else: 
                 cprint("Input hash: " + inputHash, 'white')
                 cprint("List hash : " + wordlistHash, 'white')
                 cprint("FAIL!! Password Not Found :( : " + password, 'red')
                 # If the hashes are not the same, the program prints that to the user, and continues
                 pass
   
    # This line is calling the crackHash function. The code will not run if this is removed.
    # The hash here is a placeholder, and it makes sure the input for the program is a 512 hash
    if __name__ == '__main__':
        crackHash_sha512("9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043")
           
except KeyboardInterrupt:
        cprint('Quitting! The program was interrupted by the user', 'red')   
        sys.exit()                         
except FileNotFoundError:
        cprint("Sorry, the file does not exist...", 'red')
        sys.exit()
except FileExistsError:
        cprint("Cannot create a new file, because it already exists..", 'red') 
        sys.exit()
except:
        cprint('OOOPS, there was an error. Please try again...', 'red')



    
        
