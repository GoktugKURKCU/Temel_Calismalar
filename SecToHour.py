saniye = int(input("Saniye Giriniz: "))
if saniye >= 60:
    dakika = saniye // 60
    saniye %= 60
    if dakika >= 60:
        saat = dakika // 60 
        dakika %= 60
        if saat >= 24:
            gun = saat // 24
            saat %= 24
            if gun >= 7:
                hafta = gun // 7
                gun %= 7
                if hafta >= 4:
                    ay = hafta // 4
                    hafta %= 4
                    if ay >= 12:
                        yil = ay // 12
                        ay %= 12
                        print(f"Yıl: {yil} Hafta: {hafta} Gün: {gun} Saat: {saat} Dakika: {dakika} Saniye: {saniye}")
                    else:
                        print(f"Ay: {ay} Hafta: {hafta} Gün: {gun} Saat: {saat} Dakika: {dakika} Saniye: {saniye}")
                else:
                    print(f"Hafta: {hafta} Gün: {gun} Saat: {saat} Dakika: {dakika} Saniye: {saniye}")
            else:
                print(f"Gün: {gun} Saat: {saat} Dakika: {dakika} Saniye: {saniye}")
        else:
            print(f"Saat: {saat} Dakika: {dakika} Saniye: {saniye}")
    else:
        print(f"Dakika: {dakika} Saniye: {saniye}")
else:
    print(f"Saniye: {saniye}")