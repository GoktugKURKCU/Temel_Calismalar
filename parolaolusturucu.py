
import random #Rastgele harf, sayı ve sembol için random modulü eklendi.
"""----------------------------------------------------------------------------------------------------------------------------------"""

giris = input("Parola Oluşturucuya Hoşgeldiniz. Öncelikle parolanın kaydedilmesini istiyor musunuz(Evet/Hayır): ") #Kullanıcıya şifreyi kaydedip etmeyeceği soruldu.
giris = giris.upper() #BÜYÜK-küçüm harf hatalarını engellemek için "giris" büyük harflere çevrildi.(.lower ile küçültüledebilir/tercih meselesi)
"""-----------------------------------------------------------------------------------------------------------------------------------"""
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z"] #Alfabe
symbols = ["!","'","^","#","+","$","é","%","&","/","{","(","[",")","]","=","}","?","\\","*","-","+","<",">"] #Semboller

if giris == "HAYIR": #şifre kaydedilmeyecek ise;
    print("Birazdan elde edeceğiniz parola kaydedilmeyecektir. Bu sebep ile bir yere not almanız tavsiye edilir.")
    
    basamak = int(input("Kaç basmaklı parola istiyorsunuz: ")) #Şifre kaç basamaklı?
    parola = [] # Parola da bulunması için adımlar boyu seçilen tüm elemanlar burada tutulacak

    #istenen basamak sayısı kadar dönerek, basamak sayısı*4 karakterden oluşan şifreyi oluşturacak döngü
    for basamaksayisi in range(0,basamak):
        specialNumbers = random.randint(0,9) #şifrede bulunacak rakamlar
        parola.append(specialNumbers)
        alpha = random.choice(alphabet) #şifrede bulunacak harfler
        parola.append(alpha)
        alpha2 = alpha.lower() #şifrede bulunacak küçük harfler
        parola.append(alpha2)
        symb = random.choice(symbols) #şifrede bulunacak semboller
        parola.append(symb)
        
    sonParola = [] #Kullanılacak Parola buraya kaydedilecek, buradan yazdırılacak
    
    for i in range (0,basamak): #parolayı seçecek döngü
        eleman = random.choice(parola) #parolada bulunacak elemanlar
        sonParola.append(eleman) 
    print(f"Parolanız: {sonParola}") #PAROLA  

#Parola kaydedilecek ise;
if giris == "EVET":
    print("Birazdan elde edeceğiniz parola 'parola.txt' dosyasına kaydedilecektir. Gene de bir yere not almanız tavsiye edilir.")
    basamak = int(input("Kaç basmaklı parola istiyorsunuz: "))
    parola = [] # Parola da bulunması için adımlar boyu seçilen tüm elemanlar burada tutulacak
    
    #istenen basamak sayısı kadar dönerek, basamak sayısı*4 karakterden oluşan şifreyi oluşturacak döngü
    for basamaksayisi in range(0,basamak):
        specialNumbers = random.randint(0,9) #şifrede bulunacak rakamlar
        parola.append(specialNumbers)
        alpha = random.choice(alphabet) #şifrede bulunacak harfler
        parola.append(alpha)
        alpha2 = alpha.lower() #şifrede bulunacak küçük harfler
        parola.append(alpha2)
        symb = random.choice(symbols) #şifrede bulunacak semboller
        parola.append(symb)
        
    sonParola = [] #Kullanılacak Parola buraya kaydedilecek, buradan yazdırılacak
    
    for i in range (0,basamak): #parolayı seçecek döngü
        eleman = random.choice(parola) #parolada bulunacak elemanlar
        sonParola.append(eleman)
        
    yer = input("Parolanızı nerede kullanacaksınız? (Kullanılacak Yer / Kullanıcı Adınız): ") #Parolanın tutulacağı yer
    print(f"Parolanız: {sonParola}") #PAROLA  

    #Parola Kaydı
    kayitYeri = open("parolalar.txt","a") #Parola Kayıt Yeri
    kayitYeri.write(f"\n{yer} ---> {sonParola}\n") #Her Parolayı bir alt satıra yazdıracak kod
    print("Parolalar ve kullanıcı adınız; 'parolalar.txt' adında bir dosyaya kaydedilmiştir.")