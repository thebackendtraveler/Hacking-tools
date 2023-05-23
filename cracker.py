from termcolor import cprint
import hashlib
from urllib.request import urlopen
from datetime import datetime

user_password = input("What password do you want to crack?")
wordlist = 12

password_1 = 'password'
password_2 = 'crackingmewillbedifficult'
password_3 = 'baileyiscute'
password_4 = 'tryhackme'
password_5 = 'iamafirewall'

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

cprint("The string hash value is : " + str(hash(password_1)), 'green')
cprint("The string hash value is : " + str(hash(password_2)), 'green')
cprint("The string hash value is : " + str(hash(password_3)), 'green')
cprint("The string hash value is : " + str(hash(password_4)), 'green')
cprint("The string hash value is : " + str(hash(password_5)), 'green')


