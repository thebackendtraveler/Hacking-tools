from termcolor import cprint
import hashlib
from urllib.request import urlopen
from datetime import datetime

user_password = input("What password do you want to crack?")
wordlist = 12