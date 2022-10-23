# FONKSİYONLAR
######################################
# tekrar eden ihtiyaçlar olduğunda
# tek bir amaca hizmet etmeli
# Modularity her durumda kullanılabilmeli.

(56 + 15) / 80
(17 + 45) / 70
(17 + 45) / 70
(56 + 15) / 80


def hesapla(ali, veli, deli):
    print((ali + veli) / deli)


hesapla(20, 80, 10)


# Girilen bir sayıyı 2 ile çarpan bir fonksyon tanımlayalım;
def carp(a, b):
    c = a * b
    print(c)


carp(10, 9)


# alternatif olarak print fonksiyonun içinde yazalım
def carp2(a, b):
    print(a * b)


carp2(7, 8)


# DİKKAT: burada ön tanımlı değer verdik, böylece b argümanı girilmediğinde
# b'nin değeri default olarak 1 olacaktır.
def carp3(a, b=1):
    print(a * b)


# RETURN: FONKSİYON ÇIKTILARINI GİRDİ OLARAK KULLANMAK

# Print fonksiyonun çıktısını kullanamaz mıyız?
# Deneyelim:

def carp3(a, b=1):
    print(a * b)


ab = int(carp3(5)) + 15

carp3(5)


# Eğer bir fonksiyonun çıktsını kullanmak istiyorsak ilgili fonksyionun
# sonuç değerini döndürmeliyiz. BU amaçla return yapısını kullanırız.

def carp4(a, b=1):
    return (a * b)


a = carp4(5) + 15


#############  DOCSTRİNG   #############
# Tanımladığımız fonksiyona docstring ekleme
# hazırlanan fonksyionların kullanışlı anlaşılabilir olmasını sağlamak için
# içeriğini anlatmalıyız.

# verilen iki sayıyı çarpan fonksyion yazalım

def carpiver(a=1, b=1):
    print(a * b)


carpiver()

len("merhaba")


def carpiver1(a=1, b=1):
    """

    Parameters
    ----------
    a int, float
    b int float

    Returns
    -------
    none
    """
    print(a * b)



help(carpiver1)

def carpiver2(a,b):
    """
    parameters

    Args:
        a: int, float
        b: int, float

    Returns:none

    """
    print(a*b)