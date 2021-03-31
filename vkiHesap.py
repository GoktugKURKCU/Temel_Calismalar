print("Vücut Kitle İndeksi Hesaplama Programına Hoşgeldiniz.\n\nBoyunuzu metre, kilonuzu ise kg biriminden yazınız.")
while True:    #Program kapanmaması için sonsuz döngüde
    boy = float(input("Boyunuzu Giriniz: "))
    if boy >= 2.5: #Boyun yanlış girilmesine karşı önlem
        print("Lütfen boyunuzu metre biriminden giriniz.")
        continue
    kilo = float(input("Kilonuzu Giriniz: "))
    indeks = kilo / (boy ** 2) #VKİ indeksi
    indeks = round(indeks,2) #bulunan ondalık sayıda virgülden sonra 2 hane getirecek kod (örn 25.6895 ---> 25.69)
    if indeks <= 18.5:
        print(f"Boyunuz: {boy} ve Kilonuz: {kilo}... VKİ: {indeks}---> Düşük Kilolu")
    elif indeks > 18.5 and indeks < 25:
        print(f"Boyunuz: {boy} ve Kilonuz: {kilo}... VKİ: {indeks}---> Normal Kilolu")
    elif indeks >= 25 and indeks < 30:
        print(f"Boyunuz: {boy} ve Kilonuz: {kilo}... VKİ: {indeks}---> Fazla Kilolu")    
    elif indeks >= 30 and indeks < 40:
        print(f"Boyunuz: {boy} ve Kilonuz: {kilo}... VKİ: {indeks}---> Obez")
    elif indeks >= 40:
        print(f"Boyunuz: {boy} ve Kilonuz: {kilo}... VKİ: {indeks}---> Aşırı Obez")
    else:
        break