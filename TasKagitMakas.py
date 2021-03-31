import random #taş, kağıt, makas seçeneklerini rastgele çekmek için "random" modülünü çağırdık
from time import sleep #sıra geçişlerinde beklemek için "time" modulunden "sleep" komutunu çağırdık.
while True:
    baslama = input("Taş, Kağıt, Makas Oyununa Hoş Geldin.\n\nYENİ OYUN\nKURALLAR\n\nLütfen Ne Yapacağını Belirt:")
    baslama = baslama.upper()

    if baslama == "YENİ OYUN" or baslama == "YENI OYUN" or baslama == "YENİOYUN" or baslama == "YENIOYUN":
        tur = int(input("Kaç tur oynamak istersin: "))
        pcSkor = 0
        oyuncuSkor = 0
        for baslangic in range(0,tur):
        
            #Oyundaki Seçenekler Neler?
            secenekler = ["TAŞ", "KAĞIT", "MAKAS"]

            #Oyuncu Neyi Seçecek?
            secim = input("Merhaba, Hoşgeldin. \nTAŞ, KAĞIT, MAKAS'tan hangisin seçeceksin: ")
            secim = secim.upper() #Oyuncu Seçiminin Her Zaman Büyük Harf Olmasını İstiyoruz.

            #Sıra Bilgisayarda
            print("Sıra Bilgisayarda...")
            sleep(3)

            #Bilgisayar Seçeneklerden Birini Rastgele Seçiyor.
            pcSecim = random.choice(secenekler)
            
            #Seçenekler Aynı olursa (TAŞ-TAŞ    KAĞIT-KAĞIT   MAKAS-MAKAS)
            while pcSecim == secim:
                print(f"Sizin Seciminiz: {secim} \nBilgisayarın Seçimi: {pcSecim}... \n\nİkiside aynı olduğu için Sonuç BERABERE. {pcSkor} - {oyuncuSkor}")
                break

            #Bilgisayar Güçlüyü Seçerse (TAŞ-MAKAS    MAKAS-KAĞIT     KAĞIT-TAŞ)
            while (pcSecim == "TAŞ" and secim == "MAKAS") or (pcSecim == "MAKAS" and secim == "KAĞIT") or (pcSecim == "KAĞIT" and secim == "TAŞ"):
                pcSkor += 1 
                print(f"Sizin Seciminiz: {secim} \nBilgisayarın Seçimi: {pcSecim}... Bilgisayar KAZANDI. {pcSkor} - {oyuncuSkor}")
                break

            #Siz Güçlüyü Seçerseniz (MAKAS-TAŞ   KAĞIT-MAKAS   TAŞ-KAĞIT)
            while (pcSecim == "MAKAS" and secim == "TAŞ") or (pcSecim == "KAĞIT" and secim == "MAKAS") or (pcSecim == "TAŞ" and secim == "KAĞIT"):
                oyuncuSkor += 1
                print(f"Sizin Seciminiz: {secim} \nBilgisayarın Seçimi: {pcSecim}... Siz KAZANDINIZ. {pcSkor} - {oyuncuSkor}")
                break
                

    elif baslama == "KURALLAR":
        print("KURALLAR: Oyunda 3 seçenek bulunmakta. Bunlar TAŞ, KAĞIT ve MAKAS. Bu üçlüden bir seçim yapmak zorundasınız. Taş makası kırar, makas kağıdı keser ve kağıt taşı sarar.")
        
    else:
        break
