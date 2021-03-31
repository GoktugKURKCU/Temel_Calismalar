giris = int(input("Kaç giriş yapmak istersiniz: ")) #Kaç sayı girilecek
sayi=[] #Girilecek sayıları sıralamak için liste
i = 0 #döngü başlangıç
while i < giris: #sayı giriş döngüsü
    sayiGirilen = int(input("Sayi giriniz: ")) #sayı gir
    sayi.append(sayiGirilen) #girilen sayıyı listeye ekle
    if sayiGirilen == 0: #sayı 0 a eşitse bitir
        break
    elif sayiGirilen <0: #sayı 0dan küçükse uyar,yoksay
        print("Lütfen pozitif sayı giriniz...")
        pass
    else: 
        pass #kurala uygunsa devam...
    i += 1
sayi.sort(reverse=True) #sayıları büyükten küçüğe sırala
print(sayi[1]) #en büyük 2.sayıyı yaz