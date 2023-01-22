#!/usr/bin/python3
import secrets
import time
import string
listt = string.ascii_letters + string.digits

pa = str(input("Enter your password: "))
start = time.time()
o = len(pa)
print("Running....")
while (True):
    ra = "".join(secrets.choice(listt) for i in range(o))
    if ra==pa:
        print(f"Success!!! password cracked: {ra}")
        break
end = time.time()
print(f"Time taken to crack password is {end - start} seconds")
