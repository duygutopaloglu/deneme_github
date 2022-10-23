# Pycharm Tanıtım

print("merhaba")

# fonksiyon metot farkı

# metotlar: sınıf yapılarının içerisinde tanımlanan fonksyionlardır.
# Örneğin string veri yapısının içerisinde uygulanan len fonksiyonu bir metottur.
# belirli görevleri yerine getirebilirler.

# peki ben bir sınıf yapısında kulanabileceğim metotları nereden bileceğim?

dir(str)
dir(list)

# string veri yapısında kullanılan metotlar console da çıktı.

type(dir)

"merhaba".upper()


print("merhanba")


"""
Oyunda ekrana yazdırılacak açıklamaları hazırlayalım;
Önce adımları belirleyelim:
Adım 1: Karşılama Ekranı
Adım 2: Bilgisayara rassal sayı oluşturt ( num )
Adım 3: Kullanıcıdan gelen tahminleri tutacağın boş bir liste oluştur.
Adım 4: Döngü kısmı

    X = Kullanıcıdan bilgi al --> Aldığın bilgiyi listede tut. (X)

    Eğer X = num ise
        doğru tahmin olduğunu ve bu tahmine kaç seferde ulaştığını söyle
        döngüden çık.
    dd.
        Dikkat burada ilk tahmin ve diğer tahminler olarak ikiye ayrılıyor;
        Dolayısı ile öncelikle yapılan tahminin ilk mi sonra ki mi olduğunu bulmamız lazım.
        Bunu tahmin değerlerini tuttuğumuz listenin uzunluğundan ölçebiliriz.

        Eğer ilk tahminse:
            # Alternatif 1 klasik yöntem
            Eğer X > num
                fark = X-num
            dd.
                fark = num-X

            Eğer fark> 10 ise:
                    Sıcak
            Eğer fark <10 ise:
                    Soğuk
        dd:
            Tahmin sayısı 1'den fazla ise else kısmı çalışacaktır.
            Yeni tahmin'in num ile farkını önceki tahminin num ile farkıyla kıyaslamamız lazım.

            # Alternatif 2 metotla
            e_fark = abs(num- tahminler[-2])
            y_fark = abs(num - X)

            Eğer y_fark > e_fark ise:
                uzaklaşıyorsun
            Eğer fark <10 ise:
                yakınlaşıyorsun
"""

# Adım 1 Oyuncuyu karşılama ekranı yazalım

print("Tahmin oyununa hoşgeldiniz!\n")
print("Bu oyunda bilgisayar yani ben :) 1-100 arasında bir rakam belirledim \n")
print("Eğer senin tahmin ettiğin değer ile benim belirlediğim değer arasındaki fark")
print("10'dan büyük ise, Ekranda 'Soğuk' yazacağım")
print("10'dan küçük ise, Ekranda 'Sıcak' yazacağım\n")
print("Eğer yeni tahminin bir öncekine göre uzak ise , ekranda 'Uzaklaşıyorsun :(' yazacağım")
print("Eğer yeni tahminin bir öncekine göre yakın ise , ekranda 'Yakınlaşıyorsun :)' yazacağım\n")
print("Başlıyoruz!")

# Adım 2: Bilgisayara rassal sayı oluşturt ( num )

import random

num = random.randint(1, 100)
num

# Adım 3: Kullanıcıdan gelen tahminleri tutacağın boş bir liste oluştur.
tahminler = []

# Adım 4: Döngü kısmı
while True:

    X = int(input("Bu oyunda bilgisayar yani ben :) 1-100 arasında bir rakam belirledim "
                  "\n Tahmin et nedir?"))

    # Oyuncunun belirlenen aralıkta tahminde bulunmasını söyledik.
    if X < 1 or X > 100:
        print("Lütfen 1-100 arasında tahminde bulununuz")
        continue

    # bu tahmini tahminler listesine ekleyelim
    tahminler.append(X)

    if X == num:
        # doğru tahmin olduğunu ve bu tahmine kaç seferde ulaştığını söyle.
        # döngüden çık.

        print(f"Tebrikler,tahmin ettiğim değer {num} idi"
              f"Siz bu değeri {len(tahminler)} seferde tahmin ettiniz.")
        # Doğru tahmin ettiği için döngü sonlandırılır.
        break
    else:
        # Dikkat burada ilk tahmin ve diğer tahminler olarak ikiye ayrılıyor;
        # Dolayısı ile öncelikle yapılan tahminin ilk mi sonra ki mi olduğunu bulmamız lazım.
        # Bunu tahmin değerlerini tuttuğumuz listenin uzunluğundan ölçebiliriz :)

        if len(tahminler) <= 1:
            # Eğer ilk tahminse:
            # X ile num arasında ki farkı hesapla

            ## fark hesaplama alternatif 1
            if X > num:
                fark = X - num
            else:
                fark = num - X

            if fark <= 10:
                print("Sıcak !")
            else:
                print("Soğuk !")
        else:
            # tahmin sayısı 1'den fazla ise else kısmı çalışacaktır.
            # yeni tahmin'in num ile farkını önceki tahminin num ile farkıyla kıyaslamamız lazım.
            ## fark hesaplama alternatif 2

            e_fark = abs(num - tahminler[-2])
            y_fark = abs(num - X)

            if y_fark <= e_fark:
                print("Yakınlaşıyorsun :)")
            else:
                print("Uzaklaşıyorsun :)")