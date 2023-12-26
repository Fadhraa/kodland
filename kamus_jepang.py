meme_dict = {
    "OYASUMI": "ucapan selamat tidur",
    "OHAYOU": "ucapan selamat pagi"
    "KONICHIWA": "ucapan selamat siang"
}
user = input("masukan bahasa kata bahasa jepang(gunakan huruf kapital)")
if user in meme_dict:
    arti = meme_dict[user]
    print(user,"adalah", arti)
if user not in meme_dict:
    print("kata",user,"tidak ada dala kamus")
