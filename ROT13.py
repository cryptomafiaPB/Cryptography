#!/usr/bin/python3

print("-"*20+"""
                    __                    ____     
 __________ _____  / /____    __ _  ___ _/ _(_)__ _
/ __/ __/ // / _ \/ __/ _ \  /  ' \/ _ `/ _/ / _ `/
\__/_/  \_, / .__/\__/\___/ /_/_/_/\_,_/_//_/\_,_/ 
       /___/_/                                     """+"-"*20+"\n"*3)
def rot13():
    inp = input("Enter a cipher to decode using ROT13: ")
    i= inp.lower()
    ans = []
    l = "abcdefghijklmnopqrstuvwxyz"
    l1 = "abcdefghijklm"
    l2 = "nopqrstuvwxyz"
    print("Cipher text: "+str(i))
    for elm in i:
        if elm == "{" or elm == "}" or elm == "_":
            ans.append(elm)
            continue
        ind = l.index(elm)
        if ind > 12:
            ind = ind - 13
        if elm in l1:

            ans.append(l2[ind])
        else:

            ans.append(l1[ind])
    return "".join(ans)


print(rot13())

#by cryptomafiaPB