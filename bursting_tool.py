#! /ur/bin/python

from termcolor import cprint
import pyfiglet
import sys
import requests
import random
import time
from datetime import datetime


url = sys.argv[1]
wordlist = sys.argv[2]
subdir = sys.argv[3]

# Basic user interface header
banner = pyfiglet.figlet_format("RACCOON -> BURSTER")
cprint(banner, 'blue')

#The banner with information about when the cracking starts + the hash to be cracked
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Directory bursting (subdirectories) started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

try: 
# A function that will create, open and write the found directories to a .txt file
      def write(word):
             f1 = open("write1.txt", "a")
             f1.write(word +"\n")
except FileExistsError:
      cprint("This file already exists!", 'red')
except FileNotFoundError: 
      cprint("Sorry, this file does not exist!", 'red')

try: 
# This code will open the wordlist, red the lines and split them after 11 characters.
      fo = open(wordlist, "r+")
      for i in range(14):
             word = fo.readline(11).strip()
             surl = url+word+subdir
             #print(surl)

             # This code will return all the subdirectories or the file extensions, depending on what the user selected.
             # The code will only run if the response code is 200, else it will print not found and the status code
             # The status code is 200 when Found, and 404 when Not found
             response = requests.get(surl)
             #print(response)
      if (response.status_code == 200):
             cprint("[+] Found :- " + surl, 'green')
             write(word)
      else:
             cprint("[-] Not found :- " + surl, 'red')
             pass
except TimeoutError:
       cprint("Sorry. The session timed out....", 'red')
