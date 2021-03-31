###Ucgen###
import math #Matematiksel hesaplamalar için kalabalık kod silsilesi ile uğraşmak yerine modülü ekledik(sadece mutlak değer için kullandık)
kenar1 = int(input("Kenar1: "))
kenar2 = int(input("Kenar2: "))
kenar3 = int(input("Kenar3: "))
#denklemler
a = kenar1 - kenar2
b = kenar1 + kenar2 
c = kenar1 - kenar3
d = kenar1 + kenar3
e = kenar2 - kenar3
f = kenar2 + kenar3
#düzen
a = int(math.fabs(a)) 
c = int(math.fabs(c))  ##a,c,e denklemlerinin negatif çıkması durumuna karşın mutlak değerlerini aldık.
e = int(math.fabs(e))
#Bu sayılar ile üçgen olur mu?
if (a<kenar3<b) or (c<kenar2<d) or (e<kenar1<f):
    print("Üçgen başarılı...")
    #Açısına göre üçgen
    if (kenar1**2 + kenar2**2 == kenar3**2) or (kenar2**2 + kenar3**2 == kenar1**2) or (kenar1**2 + kenar3**2 == kenar2**2):
        print("Bu bir dik üçgendir.")
    elif (kenar1**2 + kenar2**2 > kenar3**2) or (kenar2**2 + kenar3**2 > kenar1**2) or (kenar1**2 + kenar3**2 > kenar2**2):
        print("Bu bir geniş açılı üçgendir.")
    elif (kenar1**2 + kenar2**2 < kenar3**2) or (kenar2**2 + kenar3**2 < kenar1**2) or (kenar1**2 + kenar3**2 < kenar2**2):
        print("Bu bir dik üçgendir.")
    else:
        pass
else: print("Bu üçgen çizilemez.")

"""
a^2 + b^2 = c^2 ---> dik üçgende hipotenüs... 3,4,5 üçgenini ele alalım. 3^2 + 4^2 = 5^2 old. göre; 
uzun kenarın 5 değil 6 olursa bu durum, açının geniş; tam tersi ise dar açı old. anlamına gelir. 
"""