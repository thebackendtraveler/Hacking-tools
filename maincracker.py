import hashlib
from termcolor import cprint



def crackHash(inputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find file")
        
    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            cprint("SUCCESS!! Password Found: " + password, 'green')

if __name__ == '__main__':
    #crackHash("5f4dcc3b5aa765d61d8327deb882cf99")
    crackHash = input("Give me a hash to crack: ")



