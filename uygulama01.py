sorular = ['Mustafa Kemal Atatürk 1881 yılında doğmuştur.[D/Y]',
           'Mustafa Kemal Atatürk geometri kitabı yazmıştır.[D/Y]',
           'Mustafa Kemal Atatürk Lozan görüşmelerine gitmiştir.[D/Y]',
           'Mustafa Kemal Atatürk hayatında hiç evlenmemiştir.[D/Y]',
           'Mustafa Kemal Atatürk mutlak monarşi görüşünü savunmuştur.[D/Y]',]
cevaplar = ['D','D','Y','Y','Y']
puan = 0
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper():
    print("Mükemmel, cevabınız doğru!")
    puan += 1
else:
    print("Üzgünüm, yanlış cevap!")
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper():
    print("Mükemmel, cevabınız doğru!")
    puan +=1
else:
    print("Üzgünüm, yanlış cevap!")
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper():
    print("Mükemmel, cevabınız doğru!")
    puan += 1
else:
    print("Üzgünüm, yanlış cevap!")
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("Mükemmel, cevabınız doğru!")
    puan += 1
else:
    print("Üzgünüm, yanlış cevap!")
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("Mükemmel, cevabınız doğru!")
    puan += 1
else:
    print("Üzgünüm, yanlış cevap!")

    print("Tebrikler, testi tamamladınız. Toplam puanınız: "+str(puan*20))
