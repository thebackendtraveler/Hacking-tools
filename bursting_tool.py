#! /usr/bin/python

from termcolor import cprint
import pyfiglet
import sys
import requests
from datetime import datetime

# Basic user interface header
banner = pyfiglet.figlet_format("RACCOON -> BURSTER")
cprint(banner, 'blue')

# Asking the user for a url and a wordlist to use 
wordlist = input("What wordlist do you want to use?: ")
url = input("What url do you want to use?: ")

#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Looking for subdomains.... Search started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')
     
try: 
      sub_list = open(wordlist, "r").read() # The program opens the file and reads it in r mode (only reading)
      subs = sub_list.splitlines() # Then it splits the lines

      for sub in subs:
            url_to_check = f"http://{sub}." + url # Here the program is told to look for subdomains
          
            response = requests.get(url_to_check) # The programs uses the requests module to request information about subdomains
           
            if (response.status_code == 200): # HTTP status 200, means the request was successful
                  print(response)
                  cprint("Valid subdomain Found : " + url_to_check, 'green')
                  fdw = open("bursting_results.txt", "+a") # Opening an output file in +a mode to keep appending to it
                  fdw.write("\n")  # And then it writes the results from the search
                  fdw.write("A valid subdomain is: ")
                  fdw.write(url_to_check + '\n')
                  fdw.close() # Lastly, the file is closed
            else:
                  # If some requests are 404: not found, the program will continue
                  # nothing will be printed
                  pass
# To tell the program what to do when it encounters errors, the program has a complex except statement
except KeyboardInterrupt: 
      cprint("Quitting! The program was interrupted by the user.", 'red')
      sys.exit()   
except FileExistsError:
      cprint("This file already exists! The program cannot overwrite it!", 'red')
except FileNotFoundError: 
      cprint("Sorry, this file does not exist!", 'red')
except requests.ConnectionError:
      pass

print("\n") # Here the program prints an empty line to make the output look nicer

# Asking the user for a url to use, a wordlist to use and what we want to search for
url = input("What URL do you want to check?: ")
wordlist = input("What wordlist do you want to use?: ")
subdir = input("What do you want to look for?: ")

#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("Looking for subdirectories.... Search started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

try: 
# This code will open the wordlist, read the lines and split them after 11 characters.
      fo = open(wordlist, "r+") # r+ mode is for both reading and writing to a file
      for i in range(8):
          word = fo.readline(11).strip()
          surl = url+word+subdir
          #print(surl)

          # This code will return all the subdirectories 
          # The code will only run if the response code is 200, else it will print not found 
          # 200 means success and 404 means unsuccessful
          response = requests.get(surl)
         
          if (response.status_code == 200): # HTTP status 200, means the request was successful
              print(response)
              cprint("Subdirectory Found : " + surl, 'green')
              fdw = open("bursting_results.txt", "+a") # The program opens the file in +a mode to append more lines
              fdw.write("\n") # and writes the results to this file
              fdw.write("A valid subdirectory is: ")
              fdw.write(surl + '\n')
              fdw.close() # Then the program closes the file
          else:
              # If some requests are 404: not found, the program will continue
              # nothing will be printed
              pass
# Here is a complex exception to make sure the program can handle an error gracefully
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

print("\n") # Here the program prints an empty line to make the output look nicer

# Asking the user for a url to use, a wordlist to use and an extention to look for
url = input("What URL do you want to check?: ")
wordlist = input("What wordlist do you want to use?: ")
ext = input("What extension do you want to look for?: ")


#The banner with information about when the bursting starts + the URL used
cprint("_" * 50, 'blue')
cprint("URL is " + url, 'blue')
cprint("Wordfile is " + wordlist, 'blue')
cprint("File extension is " + ext, 'blue')
cprint("Looking for file extensions.... Search started at: " + str(datetime.now()), 'blue')
cprint("_" * 50, 'blue')

try: 
# This code will open the wordlist, red the lines and split them after 11 characters.
      fo = open(wordlist, "r+") # r+ mode is for both reading and writing to a file
      for i in range(8):
          word = fo.readline(20).strip()
          surl = url+word+ext
          extension = word+ext
          #print(surl)

          # This code will return all the file extensions
          # The code will only run if the response code is 200, else it will print not found 
          # 200 = success, and 404 != success
          response = requests.get(surl)
          
          if (response.status_code == 200): # HTTP status 200, means the request was successful
              print(response)
              cprint("File-extension Found : " + surl, 'green')
              fdw = open("bursting_results.txt", "+a") # The file is opened in +a to keep adding lines to it
              fdw.write("\n")
              fdw.write("A valid file-extension is: ")
              fdw.write(extension + '\n')
          else:
              # If some requests are 404: not found, the program will continue
              # nothing will be printed
              pass
# Here is a complex except statement, so the program knows what to do when it encounters an error
except KeyboardInterrupt:
       cprint("Quitting! The program was interrupted by the user.", 'red')
       sys.exit()
except TimeoutError:
       cprint("Sorry. The session timed out....", 'red')
       sys.exit()
except FileExistsError:
       cprint("This file already exists!", 'red')
       sys.exit()
except FileNotFoundError: 
       cprint("Sorry, this file does not exist!", 'red')
       sys.exit()
except TypeError: 
       cprint("Sorry... There was a type error. Try again")
       sys.exit()
      






