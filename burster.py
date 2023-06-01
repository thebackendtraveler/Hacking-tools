import requests
import random
import time
import sys
from termcolor import cprint

url = sys.argv[1]
wordlist = sys.argv[2]
ext = sys.argv[3]

def write(word):
    f1 = open("write1.txt", "a")
    f1.write(word +"\n")

fo = open(wordlist, "r+")
for i in range(2000):
    word = fo.readline(10).strip()
    surl = url+word+ext
    #print(surl)

    response = requests.get(surl)
    #print(response)
    if (response.status_code == 200):
        cprint("[+] Found :- ", surl, 'green')
        write(word)
    else:
        cprint("[-] Not found :- ", surl, 'red')
        pass