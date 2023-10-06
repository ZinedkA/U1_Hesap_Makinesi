import os
# Daha iyi bir görünüm için Terminali temizle fonksiyonu
def terminali_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# Toplama işlemi
def toplama(x, y):
    return x + y
#-----------------------------------------------------------------------------
# Çıkarma işlemi
def cikarma(x, y):
    return x - y
#-----------------------------------------------------------------------------
# Çarpma işlemi
def carpma(x, y):
    return x * y
#-----------------------------------------------------------------------------
# Bölme işlemi
def bolme(x, y):
    # Sıfıra bölme hatasını kontrol et
    if y != 0:
        return x / y
    else:
        return "Hata: Sıfıra bölme hatası"
#-----------------------------------------------------------------------------
# Ana döngü
while True:
    
    # Kullanıcıya işlem seçeneklerini gösterir
    print("Yapmak istediğiniz işlemi seçiniz:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Programdan Çıkış")

    # Kullanıcının seçimini alır
    girdi = input("Lütfen Seçiminizi Yapın (1-5): ")   
#-----------------------------------------------------------------------------
    # Çıkış seçeneğini seçip seçmediğini kontrol et
    if girdi == '5':
        print("Çıkış yapılıyor...")
        terminali_temizle()
        break
#-----------------------------------------------------------------------------
    # Kullanıcının seçimine göre işlem yap
    if girdi in ('1', '2', '3', '4'):
        # Kullanıcıdan sayıların alındığı kısım
        sayilar = []
        while True:
            sayi = input("Bir Sayı girin (çıkmak için 'q' basın): ")
            if sayi == 'q':
                break
            sayilar.append(float(sayi))
            
        # Kullanıcının seçimine göre işlemi yap ve sonucu ekrana yazdır
        sonuc = sayilar[0]
        for i in range(1, len(sayilar)):
            if girdi == '1':
                sonuc = toplama(sonuc, sayilar[i])
            elif girdi == '2':
                sonuc = cikarma(sonuc, sayilar[i])
            elif girdi == '3':
                sonuc = carpma(sonuc, sayilar[i])
            elif girdi == '4':
                sonuc = bolme(sonuc, sayilar[i])
        if girdi == '1':
            islem = 'Toplama'
        elif girdi == '2':
            islem = 'Çıkarma'
        elif girdi == 3:
            islem = 'Çarpma'
        elif girdi == 4:
            islem = 'Bölme'
        terminali_temizle()
        print(f"Girilen Sayılar: {sayilar}")
        print(f"{islem} işlemi yapıldı")
        print(f"Sonuç: {sonuc}")
        print(f" ")
    else:
        print("Hatalı Girdi. Lütfen 1-5 arasında bir sayı girin.")
