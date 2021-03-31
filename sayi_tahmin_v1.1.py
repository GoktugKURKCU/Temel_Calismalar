"""
Türkçe ve İngilizce bölümlerinin tek farkı metinlerin dilleridir, Küçük ve zorlayıcı olmayan programlarda elimden
geldiğince ingilizce kısım ekleyerek sadece yazılımda değil İngilizce de de kendimi geliştirmeye çalışıyorum. 
Ne kadar işe yarar bilemem ancak 3-5 kelime öğrettiği bir gerçek ayrıca eğlenceli oluyor.

Kodlara gelirsek; Kolay kısım bitene kadar tüm kodları açıkladım, diğer kodlar ile kolay kısmın tek farkı sayı 
aralıklarının farklı olmasıdır.
"""

import random # Aralıktaki sayıları rastgele almak için random modülünü ekledik.

print("Hoşgeldiniz/Welcome. \nLütfen oyun dilini seçiniz./Select game language.")

language = input("Dil (Türkçe/English): ") #Dil Seçimi
language = language.upper() #Karar yapılarında ki girdi kısmında sıkıntı olmaması için, girdiyi büyülttük.

while True: #Oyun bitince kapanmasın ancak sıfırlansın diye sonsuz döngüye aldık.

    #Türkçe
    if language == "TÜRKÇE" or language == "TURKCE":
        difficulty = input("Zorluk Seçiniz (Kolay, Orta, Zor): ") #Zorluk Seçimi
        difficulty = difficulty.upper()
    
        #Kolay
        if difficulty == "KOLAY":
            number = random.randint(0,10) #Kolay bilgisayarın 0-10 aralığında tercih yapmasını istedik
            health = 5 # 5 can hakkımız olacak, bunu aşağıdaki döngüde kullanacağız.
            print("Bilgisayar 0 ile 10 aralığında bir sayı tuttu ve bunu bilmenizi istiyor. Sayıyı bilmek için 5 hakkınız bulunmakta.")

            while health > 0: #Yukarda belirttiğimiz 5 canı burda kullanacağız...
                guess = int(input("Lütfen bilgisayarın tuttuğu sayıyı tahmin etmeye çalışın: ")) 

                if health == 1: #Canlar bitti ise ;
                    print(f"Maalesef bilemediniz. Tutulan sayı: {number}  Oyun Bitti.")
                    break
                elif guess == number: #Doğru Tahmin
                    print("Tebrikler. Bildiniz.")
                    break
                elif guess < number: #tahmin tutulan sayıdan küçük ise;
                    print("Daha büyük bir sayı giriniz.")
                else: #tahmin tutulan sayıdan büyük ise;
                    print("Daha küçük bir sayı giriniz.")

                health -= 1 #sayıyı bilmemiz halinde oyun biteceği için diğer her durumda 1 can kaybederiz...
    
        #Orta
        if difficulty == "ORTA":
            number = random.randint(0,50)
            health = 5
            print("Bilgisayar 0 ile 50 aralığında bir sayı tuttu ve bunu bilmenizi istiyor. Sayıyı bilmek için 5 hakkınız bulunmakta.")

            while health > 0:
                guess = int(input("Lütfen bilgisayarın tuttuğu sayıyı tahmin etmeye çalışın: "))
                if health == 1:
                    print(f"Maalesef bilemediniz. Tutulan sayı: {number}  Oyun Bitti.")
                    break
                if guess == number:
                    print("Tebrikler. Bildiniz.")
                    break
                elif guess < number:
                    print("Daha büyük bir sayı giriniz.")
                else:
                    print("Daha küçük bir sayı giriniz.")
                health -= 1

        #Zor
        if difficulty == "ZOR":
            number = random.randint(0,100)
            health = 5
            print("Bilgisayar 0 ile 100 aralığında bir sayı tuttu ve bunu bilmenizi istiyor. Sayıyı bilmek için 5 hakkınız bulunmakta.")

            while health > 0:
                guess = int(input("Lütfen bilgisayarın tuttuğu sayıyı tahmin etmeye çalışın: "))
                if health == 1:
                    print(f"Maalesef bilemediniz. Tutulan sayı: {number}  Oyun Bitti.")
                    break
                if guess == number:
                    print("Tebrikler. Bildiniz.")
                    break

                elif guess < number:
                    print("Daha büyük bir sayı giriniz.")

                else:
                    print("Daha küçük bir sayı giriniz.")

                health -= 1


    #English
    if language == "ENGLISH":
        difficulty = input("Select difficulty (Easy, Medium, Hard): ")
        difficulty = difficulty.upper()
    
        #Easy
        if difficulty == "EASY":
            number = random.randint(0,10)
            health = 5
            print("The computer select a number between 0 and 10. You must find it. You have 5 right for guessing the number.")

            while health > 0:
                guess = int(input("Please, guess the number: "))
                if health == 1:
                    print(f"Unfortunately, you didn't find the number. The number is: {number}  Game Over.")
                    break
                if guess == number:
                    print("Congratulations. You find the number.")
                    break

                elif guess < number:
                    print("You must guess bigger than: ")

                else:
                    print("You must guess smaller than: ")

                health -= 1
    
        #Medium
        if difficulty == "HARD":
            number = random.randint(0,50)
            health = 5
            print("The computer select a number between 0 and 50. You must find it. You have 5 right for guessing the number.")

            while health > 0:
                guess = int(input("Please, guess the number: "))
                if health == 1:
                    print(f"Unfortunately, you didn't find the number. The number is: {number}  Game Over.")
                    break
                if guess == number:
                    print("Congratulations. You find the number.")
                    break

                elif guess < number:
                    print("You must guess bigger than: ")

                else:
                    print("You must guess smaller than: ")

                health -= 1

        #Hard
        if difficulty == "HARD":
            number = random.randint(0,100)
            health = 5
            print("The computer select a number between 0 and 100. You must find it. You have 5 right for guessing the number.")

            while health > 0:
                guess = int(input("Please, guess the number: "))
                if health == 1:
                    print(f"Unfortunately, you didn't find the number. The number is: {number}  Game Over.")
                    break
                if guess == number:
                    print("Congratulations. You find the number.")
                    break

                elif guess < number:
                    print("You must guess bigger than: ")

                else:
                    print("You must guess smaller than: ")

                health -= 1
