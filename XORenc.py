inp = input("Enter a massage to encrypt using XOR the cheapest way to encrypt data: ")

def enc(i):
    enc_key = 'A'
    ency = "".join([chr(ord(x)^ord(enc_key)) for x in i])
    print("Encypted massage is: "+str(ency))
    decy = "".join([chr(ord(x)^ord(enc_key)) for x in ency])
    p = int(input("Decypt or not(1/2): "))
    if p==1:
        print(str(decy))
    else:
        print("Okey bye")
    

print(enc(inp))
