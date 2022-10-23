# COMPREHENSIONS
######################################

# Daha önce yaptığımız örnek:

maaslar = [1000, 2000, 3000, 4000]


def zam(x):
    return x + x * 20 / 100


for m in maaslar:
    print(zam(m))


# 3000 üstü % 15 zam yapan fonksiyon yazalım
def ust_zam(x):
    return x + x * 15 / 100


# 3000 altı % 20 zam yapan fonksiyon yazalım
def alt_zam(x):
    return x + x * 20 / 100


maaslar = [1000, 2000, 3000, 4000, 5000]
yeni_maas = []
for m in maaslar:
    if m >= 3000:
        yeni_maas.append(alt_zam(m))
    else:
        yeni_maas.append(ust_zam(m))

# aynı şeyi comprehension ile nasıl ifade ederiz?

# maaşların tamamını 2 katına alalım
maaslar = [1000, 2000, 3000, 4000, 5000]
yeni_bos = []
for m in maaslar:
    yeni_bos.append(m * 2)

maaslar = [m * 2 for m in maaslar]

[maas * 2 for maas in maaslar]

maaslar = [i**2 for i in maaslar]

# maaşı 3000'den küçük olanlara zam yapılması halinde;
[ust_zam(maas) for maas in maaslar if maas < 3000]

# 3000'den küçük olanlara %20 büyük olanlar %15 zam yapılırsa

maaslar = [ust_zam(maas) if maas < 3000 else alt_zam(maas) for maas in maaslar]

# bir satır aslında şu ifadeye denk geliyor:

yeni_maas = []
for m in maaslar:
    if m >= 3000:
        yeni_maas.append(alt_zam(m))
    else:
        yeni_maas.append(ust_zam(m))

# örnek

ogrenciler = ["ali", "ayse", "yasemin", "kaan", "hale"]

gecen_ogrenci = ["ali", "yasemin", "hale"]
kalan_ogrenci = ["ayse", "kaan"]

for i in ogrenciler:
    print(i)

[i for i in ogrenciler]
[ i.upper() for i in ogrenciler if i in gecen_ogrenci  ]

[i.upper() if i in gecen_ogrenci else i for i in ogrenciler ]

[i.upper()+"_geçti" if i in gecen_ogrenci else i+"_kaldı" for i in ogrenciler]
# verilen oğrenci listesinde geçen öğrencilerin ismi büyük olsun
[w.upper() for w in ogrenciler if w in gecen_ogrenci]

# geçenler büyük olsun ama kalanlar küçük olarak listede olsun
[w.upper() if w in gecen_ogrenci else w.lower() for w in ogrenciler]

# hadi geçen öğrencilerin yanına "_geçti", kalan öğrencilerin yanına "_kaldı" yazalım.
[w + "_geçti" if w in gecen_ogrenci else w + " kaldı" for w in ogrenciler]

#######################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
#######################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# Veri setini çağıralım

import seaborn as sns

df = sns.load_dataset("car_crashes")

# bu datada hangi değişkenler varmış bakalım
# df.columns bir dataframe de bulunan değişkenlerin isimlerini getirir.
df.columns

# Bütün değişkenlerin isimlerini büyük hale getirelim

# 1. yol
A = []
for col in df.columns:
    A.append(col.upper())
df.columns = A

# 2.yol
df.columns = [col.upper() for col in df.columns]

df.columns=[sutun.upper() for sutun in df.columns]

# İsminin başında INS olan değişkenlere "FLAG" değerini ekleyelim.
# olmayanlara ise NO_FLAG ekleyelim.

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

df.columns

# başında INS olan değişkenleri çağıralım
[sutun for sutun in df.columns if "INS" in sutun]

["FLAG_"+sutun if "INS" in sutun else sutun for sutun in df.columns]

["FLAG_"+sutun if "INS" in sutun else "NO_FLAG_"+sutun for sutun in df.columns]





[col for col in df.columns if "INS" in col]

# başında INS olanlara FLAG ekleyelim

["FLAG_" + col for col in df.columns if "INS" in col]


# başında INS olmayanlara NO_FLAG ekleyelim, olanlara FLAG ekleyelim

["FLAG_" + col if "INS" in col else "NO_FLAG" + col for col in df.columns]


#######################
# Categorical Değişkenlerin Başına CAT yazmak.
#######################


# before:
# ['total',
# 'speeding',
# 'alcohol',
# 'not_distracted',
# 'no_previous',
# 'ins_premium',
# 'ins_losses',
# 'abbrev']

# after:
# ['TOTAL',
#  'SPEEDING',
#  'ALCOHOL',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM',
#  'INS_LOSSES',
#  'CAT_ABBREV']

# değişkenlerin tiplerine bakalım
df.head(5)
# mesela alkol değişkeninin tipine bakalım
df["ALCOHOL"].dtype

df["ABBREV"].dtype

# kategorik değişkenler obje olarak değerlendirilir. veri tipi = object

# veri tipi kategorik olan değişkeni belirleyelim

[col for col in df.columns if df[col].dtype == "O"]



# kategorik depğişkenin başına CAT_ yazalım

["CAT_" + col for col in df.columns if df[col].dtype == "O"]

# E diğer sutunlar aynı kalsın bunu görelim
["CAT_" + col if df[col].dtype == "O" else col for col in df.columns]


