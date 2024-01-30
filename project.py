import random

def gen_pass():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    password_length = 10
    for i in range(password_length):
        password += random.choice(elements)

    return password
def flip_coins():
    coins = random.randint(1,2)
    if coins == 1:
        return "Angka"
    else:
        return "Gambar"
sampah_organic = ['daun','makanan sisa','kotoran hewan',
                  'cangkang telur','sayur dan buah busuk',
                  'kayu', 'kertas']
sampah_anorganic = ['plastik','karet','kaca','kaleng','besi',
                    'seterofoam','kresek','botol plastik']

