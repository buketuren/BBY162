#BuketÜren

print("Adam Asmaca Oyununa Hoşgeldiniz!")
print("Oyunda bazı hayvanların isimlerini tahmin etmeniz gerekmektedir.!")

import random
wordList = random.choice(["Kedi","Köpek","Fare","Kuş","Aslan","Kaplan","Balık","Fil","Zürafa","At"])
wordList = wordList.upper()
canSayisi = 4
words = []
harfSayisi = "_"

for word in wordList:

    words.append(harfSayisi)

print(words)

while canSayisi > 0:

    i = 0

    tahmin = input("\nbir harf girin: ")
    tahmin = tahmin.upper()

    if tahmin in wordList:
        for kontrol in wordList:
            if wordList[i] == tahmin:
                words[i] = tahmin
            i += 1

        print("")
        print(words)
        print("\n \"%s\" harfi " %tahmin)

    else:
        canSayisi -= 1
        print("")
        print(words)
        print("\n\"%s\" harfi yanlış. Başka harf girin" % tahmin)
        print(canSayisi, "Canınız Kaldı")

    if canSayisi == 0:
        print("Maalesef bilemediniz!")
        break


    if harfSayisi not in words:
        print("\nTebrikler! Doğru tahmin")
        break



