#! /ur/bin/python

from termcolor import cprint
import pyfiglet
import sys
import requests
import random
import time
from datetime import datetime

# Basic user interface header
banner = pyfiglet.figlet_format("RACCOON -> BURSTER")
cprint(banner, 'blue')

url = input("What URL do you want to check?: ")
wordlist = input("What wordlist do you want to use?: ")
subdir = input("What subdirectory do you want to look for?: ")

#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Directory bursting (subdirectories) started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

try: 
      def write(word):
          """
              A function that will create, open and write the found directories to a .txt file
          """
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


print("\n")

url = input("What URL do you want to check?: ")
wordlist = input("What wordlist do you want to use?: ")
ext = input("What extension do you want to look for?: ")


#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Directory bursting (file extensions) started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

try: 
      def write(word):
          """
              A function that will create, open and write the found directories to a .txt file
          """
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
          surl = url+word+ext
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
