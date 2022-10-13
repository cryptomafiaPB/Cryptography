import hashlib
print("+"+"-"*40+"+\n        TEXT(ASCII) to HASH(MD5)\n+"+"-"*40+"+")
strr = input("Enter a massage: ")

result = hashlib.md5(strr.encode())

print("Hash of ",strr," is : ", end="")
print(result.hexdigest())
