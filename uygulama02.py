sorular = ['Sinekli Bakkal romanının yazarı aşağıdakilerden hangisidir?',
           'Hangi ülkenin iki tane başkenti vardır?',
           'Romen rakamında hangi sayı yoktur?',
           'Aspirinin hammaddesi nedir?',
           'Üç büyük dince kutsal sayılan şehir hangisidir?']

cevaplar = ['B', 'A', 'A', 'A', 'B']
cevapA = ['Reşat Nuri Güntekin','Güney Afrika','0','Söğüt','Mekke']
cevapB = ['Halide Edip Adıvar','Senegal', '50', 'Köknar', 'Kudüs']
cevapC = ['Ziya Gökalp', 'İspanya', '100', 'Kavak', 'Roma']
cevapD = ['Ömer Seyfettin', 'Şili', '1000', 'Meşe', 'İstanbul']
puan= 0
for i in range(len(sorular)):
    print("Soru " + str(i+1)+":"+sorular[i])
    print("A) " + cevapA[i])
    print("B) " + cevapB[i])
    print("C) " + cevapC[i])
    print("D) " + cevapD[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan += 1
print("Tebrikler,testi Tamamladınız!")
print("Aldığınız not: " + str(int((puan / len(sorular)) * 100)))