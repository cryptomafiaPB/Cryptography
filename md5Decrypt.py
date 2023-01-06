#!/usr/bin/python3
print("-" * 20 + """
                    __                    ____     
 __________ _____  / /____    __ _  ___ _/ _(_)__ _
/ __/ __/ // / _ \/ __/ _ \  /  ' \/ _ `/ _/ / _ `/
\__/_/  \_, / .__/\__/\___/ /_/_/_/\_,_/_//_/\_,_/ 
       /___/_/                                     """ + "-" * 20 + "\n" * 3)
import hashlib
import os
def crack(hash):
    print(os.listdir())
    f = str(input("Enter file containing passwords: "))
    try:
        fileopen = open(f, "r")
    except:
        print("File doesn't exist!!")
    flag = 0
    for password in fileopen:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == hash:
            flag = 1
            r = password
            print("Yes")
    if flag == 1:
        print("Password Found!!!    :)\nPassword for " + hash + " ==> " + r)
    else:
        print("Password NOT Found     :(")
i = str(input("Enter a md5 hash :  ")).strip()
crack(i)
#github = @cryptomafia
