#! /usr/bin/python

from termcolor import cprint
import pyfiglet
import sys
import requests
from datetime import datetime

# Basic user interface header
banner = pyfiglet.figlet_format("RACCOON -> BURSTER")
cprint(banner, 'blue')

wordlist = input("What wordlist do you want to use?: ")
url = input("What url do you want to use?: ")

#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Looking for subdomains.... Search started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')
     
try: 
      sub_list = open(wordlist, "r").read()
      subs = sub_list.splitlines()

      for sub in subs:
            url_to_check = f"http://{sub}." + url
          
            response = requests.get(url_to_check)
            print(response)
            if (response.status_code == 200):
                  cprint("Valid subdomain Found : " + url_to_check, 'green')
                  fdw = open("bursting_results.txt", "+a")
                  fdw.write("\n")
                  fdw.write("A valid subdomain is: ")
                  fdw.write(url_to_check + '\n')
                  fdw.close()
            else:
                  cprint("Valid subdomain Not found : " + url_to_check, 'red')
                  pass
except KeyboardInterrupt: 
      cprint("Quitting! The program was interrupted by the user.", 'red')
      sys.exit()   
except FileExistsError:
      cprint("This file already exists! The program cannot overwrite it!", 'red')
except FileNotFoundError: 
      cprint("Sorry, this file does not exist!", 'red')
except requests.ConnectionError:
      pass


url = input("What URL do you want to check?: ")
wordlist = input("What wordlist do you want to use?: ")
subdir = input("What subdirectory do you want to look for?: ")

#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Looking for subdirectories.... Search started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

try: 
# This code will open the wordlist, read the lines and split them after 11 characters.
      fo = open(wordlist, "r+")
      for i in range(8):
          word = fo.readline(11).strip()
          surl = url+word+subdir
          #print(surl)

          # This code will return all the subdirectories 
          # The code will only run if the response code is 200, else it will print not found 
          # 200 means success and 404 means unsuccessful
          response = requests.get(surl)
          print(response)
          if (response.status_code == 200):
              cprint("Subdirectory Found : " + surl, 'green')
              fdw = open("bursting_results.txt", "+a")
              fdw.write("\n")
              fdw.write("A valid subdirectory is: ")
              fdw.write(surl + '\n')
          else:
              cprint("Subdirectory not found : " + surl, 'red')
              pass
except KeyboardInterrupt:
       cprint("Quitting! The program was interrupted by the user.", 'red')
       sys.exit()
except TimeoutError:
       cprint("Sorry. The session timed out....", 'red')
except PermissionError: 
       cprint("You are not root, and you don't have permission to do this!..")
except FileExistsError:
       cprint("This file already exists!", 'red')
except FileNotFoundError: 
       cprint("Sorry, this file does not exist!", 'red')


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
# This code will open the wordlist, red the lines and split them after 11 characters.
      fo = open(wordlist, "r+")
      for i in range(8):
          word = fo.readline(20).strip()
          surl = url+word+ext
          #print(surl)

          # This code will return all the file extensions
          # The code will only run if the response code is 200, else it will print not found 
          # 200 = success, and 404 != success
          response = requests.get(surl)
          #print(response)
          if (response.status_code == 200):
              cprint("File-extension Found : " + surl, 'green')
              fdw = open("bursting_results.txt", "+a")
              fdw.write("\n")
              fdw.write("A valid file-extension is: ")
              fdw.write(surl + url ,'\n')
          else:
              cprint("File-extension Not found : " + surl, 'red')
              pass
except KeyboardInterrupt:
       cprint("Quitting! The program was interrupted by the user.", 'red')
       sys.exit()
except TimeoutError:
       cprint("Sorry. The session timed out....", 'red')
except FileExistsError:
       cprint("This file already exists!", 'red')
except FileNotFoundError: 
       cprint("Sorry, this file does not exist!", 'red')






