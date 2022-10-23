# NUMPY
#############################################

# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

# low level - high level
a = [1,2,3,4]
b = [2,3,4,5]
type(b)
ab = []
# verilen iki listede ki aynı indekste bulunan elemaların çarpımını bir boş listede tutalım
# low level

for i in range(len(a)):
    ab.append(a[i]*b[i])

ab

# high level
import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

ab = a*b

# a nın tipine bakalım
a = np.array([1, 2, 3, 4])
type(a)

# kullanılan numpy'ın versiyonuna bakalım
np.__version__

# liste ile np.array farkı ;

# python list
python_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numpy array
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Python listesi :", python_list)

print("Numpy dizisi :", numpy_array)

# 10 sıfırdan oluşan array oluşturalım
np.zeros(10, dtype=int)
np.zeros((3, 4))

# 0 ile 10 aralığında 10 tane rassal integer sayı üret.
np.random.randint(0, 10, size=10)
np.random.randint(0, 10, (5, 5))

# ortalaması 10 standart sapması 4 olan 3 e 4 lük matris oluştralım
np.random.normal(10, 4, (3, 4))

#############################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#############################################
a = np.random.randint(5, 10, size=10)
b = np.random.randint(-5, 10, (3, 5))

# ndim: boyut sayısı
a.ndim
b.ndim

# shape: boyut bilgisi
a.shape
b.shape

# size: toplam eleman sayısı
a.size
b.size

# dtype: array veri tipi
a.dtype
b.dtype

#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################
# 1 den 10 a kadar sayı üret
np.arange(1, 10)

# yeniden şekillendir diyerek 3x3 lük matris oluşturduk
np.arange(1, 10).reshape((3, 3))

# sizde 2'den 80' e kadar giden 6 satırlık 13 sütunluk matris oluşturun.
np.arange(2, 80).reshape((6, 13))
np.arange(2, 80).reshape((39, 2))

#############################################
# Index Seçimi (Index Selection)
#############################################

a = np.random.randint(10, size=10)
a[0]
a[-2]

a[0] = 9.9
a

# matris üzerinden gidelim
m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1,3]

m[1, 1]
m[2, 1]

m[2, 3] = 9999

# Dikkat !!!
m[2, 3] = 2.9

m[:, 0]
m[1, :]

m[0:2, 0:3]

# 8,4,1 7,2,4 getirin
m[1:,-3:]

#############################################
# Step
#############################################
# Eğer amacımız çeşitli adımlarla bir işlem yapmak ise;
# step metotunu kullanabiliriz.

step = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 12den 10'a kadar 10 dahil 2 şer 2 şer git
step[1:10:2]
step[2:6:1]

#############################################
# Fancy Index
#############################################
# daha karmaşık işlemleri arka planda yapmamızı sağlar.

v = np.arange(0, 30, 3)

# verilen array'in 1 2 ve 3. indekslerine şu şekilde gidebilirim;
v[1]
v[2]
v[3]

# yukarıda ki gibi yapmak yerine catch isimli bir liste tanımlayıp
# bu listeyi v[catch] yaparak çağırırsak fancy index yapmış oluyoruz.
yakala = [1, 7, 3]

v[yakala]

type(v)
type(yakala)

# SORU sizde verilen listenin 3 5 ve 7 indekslerini getirin
deneme = [4, 7, 2]
v[deneme]

# peki listede aynı yöntem olur mu ?
liste = [3, 5, 7, 8, 9]
cagir = [1, 2, 3]
liste[cagir]

m = np.arange(9).reshape((3, 3))

m[2, 1:3]

# 0'dan 1' e kadar 1. ve 2. sutunlar gelsin
m[0:1, [1, 2]]

#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#############################################

v = np.array([1, 2, 3, 4, 5])
v
# verilen array de bir şartımız olsun
# mesela 3 ten küçük büyük durumuna bakalım
#normalde ;

ab = []

# Klasik olarak yolu bu ;

for i in v:
    if i < 3:
        ab.append(i)

ab

# Numpy ile ise bu kadar basit;

# iç parantezde ki v < 3  bool yani true false dönüyor,
# böylece basit bir şekilde işlem tamam.
v < 3

v[v < 3]
v[v >= 3]
v[v <= 3]
v[v == 3]

# Bu işlemi yapabilmesinin temel sebebi fancy index kavramı aslında
# array içerisinde true false ifadeleri sorgulayıp  kullanocının talebini yanıtlamış oluyor.

#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################

v = np.array([1, 2, 3, 4, 5])

# bütün elemanları 5' e böl
v / 5

# bütün elemanları 5/10 ile çarp.
v * 5 / 10

# bütün elemanların karesini al
v ** 2

# bütün elemanlardan 1 çıkar.
v - 1

v * 0.3

# yukarıdaki işlemlerin metot karşılıkları ;

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)

