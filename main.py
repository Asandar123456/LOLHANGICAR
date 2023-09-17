import random


lol_karakterler = [
    "Ahri", "Yasuo", "Darius", "Lux", "Zed", "Jinx", "Thresh", "Ezreal", "Ashe", "Lee Sin",
    "Annie", "Garen", "Katarina", "Orianna", "Morgana", "Jax", "Riven", "Vayne", "Nasus",
    "Teemo", "Leona", "Draven", "Fiora", "Malphite", "Ryze", "Sona", "Akali", "Vladimir",
    "Kennen", "Kassadin", "Xayah", "Kha'Zix", "Aatrox", "Samira", "Irelia", "Camille", "Varus"
]


def rastgele_karakter_sec():
    return random.choice(lol_karakterler)


secilen_karakter = rastgele_karakter_sec()
print("Hangi Aptal Çar:", secilen_karakter)
