while True:
    secim = input("""
    1-Örnek Fibonacci Dizisi
    2-Girilen Değere Kadar Olan Fibonacci Dizisi
    3-Fibonacci Dizisinin n'inci Elemanı
    4- x Sayısı Fibonacci Dizisinin Elemanı mı ve Yeri ya da Aralığı Nedir?
    Seçiniz: """)
    if secim == "1": #Örnek Fibonacci Dizisi
        fibo = [1]
        fiboElemanı = 1
        for i in range(1,10):
            fibo.append(fiboElemanı)
            fiboElemanı = fibo[i-1] + fibo[i]
        print(f"Örnek Fibonacci Dizisi: {fibo}")
    elif secim == "2":
        istenenDeger = int(input("Kaçıncı Değere Kadarlık Diziyi İstiyorsunuz: "))
        if istenenDeger > 0:
            fibo = [1]
            fiboElemanı = 1
            for i in range(1,istenenDeger):
                fibo.append(fiboElemanı)
                fiboElemanı = fibo[i-1] + fibo[i]
            print(f"İstenen Fibonacci Dizisi: {fibo}")
        else: print("Hatalı Giriş Yaptınız...")
    elif secim == "3":
        istenenDeger = int(input("Kaçıncı Değeri Görmek İstiyorsunuz: "))
        if istenenDeger > 0:
            fibo = [1]
            fiboElemanı = 1
            for i in range(1,istenenDeger):
                fibo.append(fiboElemanı)
                fiboElemanı = fibo[i-1] + fibo[i]
            print(f"İstenen Değer: {fibo[-1]}")
        else: print("Hatalı Giriş Yaptınız...")
    elif secim == "4":
        sorulan = int(input("Dizide Varlığını Merak Ettiğiniz Sayı: "))
        if sorulan > 0:
            fibo = [1]
            fiboElemanı = 1
            for i in range(1,150):
                fibo.append(fiboElemanı)
                fiboElemanı = fibo[i-1] + fibo[i]
            if sorulan in fibo:
                print(f"Girdiğiniz Sayı: {sorulan} ---> Dizide mi: EVET ---> Yeri: {(fibo.index(sorulan)+1)} ")
            else: 
                fibo.append(sorulan)
                fibo.sort()
                print(f"Girdiğiniz Sayı: {sorulan} ---> Dizide mi: HAYIR ---> Bulunduğu Aralık: {(fibo.index(sorulan))}-{(fibo.index(sorulan)+1)}") 
        else: print("Hatalı Giriş Yaptınız...")    
    else: #Hatalı Giriş
        print("Hatalı Giriş Yaptınız...")