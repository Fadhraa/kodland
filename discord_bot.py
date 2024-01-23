import random
source = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang = int(input("masukan panjang password: "))
password = ""

for i in range(panjang):
    password += random.choice(source)
print("password anda:", password)