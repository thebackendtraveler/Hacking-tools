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

#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("Directory bursting (subdomain)) started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')
     
try: 
      sub_list = open("subdom.txt", "r").read()
      subs = sub_list.splitlines()

    
except FileExistsError:
      cprint("This file already exists!", 'red')
except FileNotFoundError: 
      cprint("Sorry, this file does not exist!", 'red')

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}" 

    try:
         response = requests.get(url_to_check)
         cprint(response, 'green')

    except requests.ConnectionError:
         pass
    
    else: 
         print("Valid domain: ", url_to_check)
         
         #print("Writing to file..")
         fdw = open("subdomain.txt", "+a")
         fdw.write("\n")
         fdw.write("A valid subdomain is: ")
         fdw.write(url_to_check + '\n')

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
          f1 = open("subdirectory.txt", "+a")
          f1.write(word +"\n")
except PermissionError: 
     cprint("You are not root, and you don't have permission to do this!..")
except FileExistsError:
      cprint("This file already exists!", 'red')
except FileNotFoundError: 
      cprint("Sorry, this file does not exist!", 'red')

try: 
# This code will open the wordlist, read the lines and split them after 11 characters.
      fo = open(wordlist, "r+")
      for i in range(8):
          word = fo.readline(11).strip()
          surl = url+word+subdir
          #print(surl)

          # This code will return all the subdirectories or the file extensions, depending on what the user selected.
          # The code will only run if the response code is 200, else it will print not found and the status code
          # The status code is 200 when Found, and 404 when Not found
          response = requests.get(surl)
          print(response)
          if (response.status_code == 200):
              cprint("Subdirectory Found : " + surl, 'green')
              write(word)
          else:
              cprint("Subdirectory not found : " + surl, 'red')
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
          f1 = open("fileextensions.txt", "+a")
          f1.write(word + ext + "\n")
except FileExistsError:
      cprint("This file already exists!", 'red')
except FileNotFoundError: 
      cprint("Sorry, this file does not exist!", 'red')

try: 
# This code will open the wordlist, red the lines and split them after 11 characters.
      fo = open(wordlist, "r+")
      for i in range(8):
          word = fo.readline(20).strip()
          surl = url+word+ext
          #print(surl)

          # This code will return all the subdirectories or the file extensions, depending on what the user selected.
          # The code will only run if the response code is 200, else it will print not found and the status code
          # The status code is 200 when Found, and 404 when Not found
          response = requests.get(surl)
          #print(response)
          if (response.status_code == 200):
              cprint("File-extension Found : " + surl, 'green')
              write(word)
          else:
              cprint("File-extension Not found : " + surl, 'red')
              pass
except TimeoutError:
       cprint("Sorry. The session timed out....", 'red')





