import requests
import sys
from termcolor import cprint
from datetime import datetime

sub_list = open("subdom.txt", "r").read()
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}" 

    try:
         requests.get(url_to_check)

    except requests.ConnectionError:
         pass
    
    else: 
         print("Valid domain: ", url_to_check)
         
         #print("Writing to file..")
         fdw = open("subdomain.txt", "+a")
         fdw.write("\n")
         fdw.write(url_to_check + '\n')


         






          