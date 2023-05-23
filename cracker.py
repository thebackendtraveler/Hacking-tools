from termcolor import cprint
import hashlib
from urllib.request import urlopen
from datetime import datetime

user_password = input("What password do you want to crack?: ")
wordlist = 'wordlist.txt'


def crackHash(password):
    try:
        wordlist = open("wordlist.txt", "r")
    except:
        print("Could not find file")
        
    for password in wordlist:
        encPass = user_password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == password:
            print("Password Found: " + password)
    
    if user_password in wordlist:
        print('Password Found')

if __name__ == '__main__':
    crackHash = input("What password do you want to crack?: ")


def crackHash(inputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find file")
        
    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print("Password Found: " + password)

if __name__ == '__main__':
    crackHash("22c276a05aa7c90566ae2175bcc2a9b0")

#password_1 = 'password'
#password_2 = 'crackingmewillbedifficult'
#password_3 = 'baileyiscute'
#password_4 = 'tryhackme'
#password_5 = 'iamafirewall'

#def hash(password):
    #result = hashlib.sha1(password.encode())
    #return result.hexdigest()

#cprint("The string hash value is : " + str(hash(password_1)), 'green')
#cprint("The string hash value is : " + str(hash(password_2)), 'green')
#cprint("The string hash value is : " + str(hash(password_3)), 'green')
#cprint("The string hash value is : " + str(hash(password_4)), 'green')
#cprint("The string hash value is : " + str(hash(password_5)), 'green')


