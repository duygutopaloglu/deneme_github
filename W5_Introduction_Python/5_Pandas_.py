# PANDAS
#############################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda

#############################################
# Pandas Series
#############################################
# veri manüplasyonu ve veri analizi için yazılmış açık kaynak kodlu python kütüphanesidir.
# Ekonometri ve finansal çalışmalar için doğmuştur.
# Panel data analizi ifadesinin kısaltılmış halidir ancak veri maniplasyonu ve veri analizi ile ilişkilendirilir.
# Odaklandığı şey numpy'ın farklı tip veri içermeme kısıtını!! ortadan kaldırmak
# index bilgisi olsun ama farklı tip veri olsun

import pandas as pd

s = pd.Series([10, 88, 3, 4, 5])
# bir liste üzerinden seri oluşturudum
type(s)

# değerlerin aralığı ve adım miktarı
s.index

# veri yapsının tipi
s.dtype

# Boyutu
s.size

s.ndim
s.values
s.head()
s.tail(3)

#############################################
# Veri Okuma (Reading Data)
#############################################

df = pd.read_csv("1.datasets/titanic.csv")

deneme = pd.read_csv(r"G:\Drive'ım\ML\1.datasets\titanic.csv")

# https://www.kaggle.com/competitions/titanic/data
#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import pandas as pd

df = pd.read_csv('1.datasets/titanic.csv')

df.columns
# dataframe'in başından ilk 5 satırı göster
df.head()

# dataframe'in sonundan 5 satırı göster
df.tail()

# dataframe'in yapısı boyut bilgisi
df.shape

# dataframe'de bulunan değişkenler ve bu değişkenlerin veri yapısı
df.info()

# dataframe'in sutunlarının isimleri
df.columns

# dataframe'in index yapısı 0 dan başlayıp şuraya kadar şu aralıklarla
df.index

# dataframe'i analiz etmek için değişkenlerin sayı ortalama vb bilgilerinin transpoze alınmış hali
df.describe().T

# dataframe'de boş hücre var mı? sorusunun cevabı.
# Burada isnull önemli
df.isnull()
df.isnull().values
df.isnull().values.any()

# Değişkenlerde ki eksik değer sayısını getirir.
df.isnull().sum()

# bir kategorik değişkenin sınıf bilgilerine erişmek için;
df["Sex"].value_counts()

# köşeli parantez kullanıldığı anda index , slice, fancy index, değişken seçme işlemi yapılabiliriz.
df["Sex"]

#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#############################################

# - Index Üzerinde İşlemler
# - Değişkeni Indexe Çevirmek
# - Indexi Değişkene Çevirmek
# - Değişkenler Üzerinde İşlemler
# - Value'lar Üzerinde İşlemler
# - iloc & loc
# - Koşullu Seçim (Conditional Selection)

df.head()

type(df)

#######################
# Index Üzerinde İşlemler
#######################
# Bir data set olduğu için hem satırlar yani satır numaraları
# hemde sütunlar yani değişkenler üzerinde işlem yapabiliriz.

# sütun bilgilerine yani değişkenlere erişmek için
df.columns

# satır bilgilerine erişmek için
df.index

# belirli satırda ki verilere ulaşmak istesek
df[0:20]

# herhangi bir indexi silmek istersek
# axis =1 sutunlara göre bak axis = 0 satırlara göre bak demek.
df.drop(0, axis=0).head()

# birden fazla indeksi silmek istersek;
# silinecek indeksleri listeye aldık
delete_indexes = [1, 3, 5, 7]
# bu listeyi silmesi için drop fonksiyonuna verdik
df.drop(delete_indexes, axis=0).head(10)

# yaptığımız değişikliklerin kalıcı olmasını istersek inplace = True dememiz yeterli
df.drop(delete_indexes, axis=0, inplace=True)
df = df.drop(delete_indexes, axis=0)
#######################
# Değişkeni Indexe Çevirmek
#######################
import pandas as pd
df = pd.read_csv('1.datasets/titanic.csv')

# passengerId'ye göre sıraladım
df.sort_values("PassengerId").head()

# sıralanmış halini tekrar df' e ataak isrtersem
df = df.sort_values("PassengerId")

# değişkeni indekse atama işlemim, df.index'e passenger ıd'yi atadım
df.index

df["PassengerId"]

df.index = df["PassengerId"]

df.head()

# alternatif örnek
df.index = df["Pclass"]

# passenger ıd değişkenini!! sildim.

df.drop("PassengerId", axis=1).head()

# aleternatif örnek
df.drop("Pclass", axis=1).head()

# alternatif yol
# df'in değişkenlerinden passenger ıd dışında kalanların tamamını seç
# ve df tekrar kendine ata
df.loc[:, df.columns != 'PassengerId'].head()

df = df.loc[:, df.columns != 'PassengerId'].head()
df.columns

# alternatif yol
# passenger ıd'yi sil ve kalıcı olarak df e ata
df.drop("PassengerId", axis=1, inplace=True)
df.columns

df.drop("Pclass", axis=1, inplace=True)
df.columns

#######################
# Indexi Değişkene Çevirmek
#######################

# bak şimdi şu müthiş bir şey;
# tek başına aşağıda ki kodu çalıştırdığımızda az önce passenger ıd'yi sildiğimiz için hata verir.
df["PassengerId"]

# ancak kodu bu şekilde yazarsak python'a şunu diyoruz
# ben bu dataframe yeni değişken ekliyorum. Bunu ekle
df["PassengerId"] = df.index

df["Pclass"] = df.index

# az önce passenger ıd'yi değişken getirip eklemiştim ya
# peki ben onu kaldırmak istersem ?
# drop ile silerim, satırları kontrol etmesi için axis 1
df.drop("PassengerId", axis=1, inplace=True)

df.drop("Pclass", axis=1, inplace=True)

# 2. yol
# index'te yer alan ifadeyi değişkene çevirir ve index resetlenir.
df.reset_index().head()

# düzelttiğim df'i tekrar kendisine atayarak kalıcı hale getirdim.
# kalıcı hale getirmek için başka ne yapabilirdim?

df = df.reset_index()


#######################
# Değişkenler Üzerinde İşlemler
#######################
# bir değişkenin dataframe'de varlığını sorgulamak istersek
"Age" in df

# BURASI ÇOK ÖNEMLİ BİR ŞEY, ŞÖYLE;

# Age değişkenini seçmek istersek şu şekilde bir kod yazabiliriz.
# Dikkat;
df["Age"].head()

# Yukarıda ki kodun tipini kontrol edersek
# değişkenin tipini pandas.core.series.Series haline getirdiğini gözlemleriz.
# Bu durumda dataframe için yazılan fonksiyonlar bu değişken üzerinde uygulanamaz.

type(df["Age"])
type(df)

# Yukarıda  aktarılan durumu engellemek ve
# bir dataframe'den bir değişkeni yine dataframe yapısı ile almak için
# çift köşeli parantez (liste ! yani fancy index aslında ) kullanmalıyız.
# Böylece seçilen değişkenin tipi dataframe olarak kalır.
df[["Age"]].head()

type(df[["Age"]])

dir(pd.core.frame.DataFrame)

df.columns

# bir değişkeni seçmenin alternatif yolu olarak şunu kullanabiliriz.
df.PassengerId.head()
df.Pclass
df.PassengerId

# Birden fazla değişkeni seçmek için;
df[["Age", "PassengerId"]].head(10)

# alternatif yol, değişkenleri liste olarak belirlemek
col_names = ["Age", "Embarked", "Ticket"]
# sonrada bu lsteyi çağırmak
df[col_names].head()
type(df[col_names])

# veri setine yeni değişken eklemek
# dataframe yeni değişken ekle bu değişkenin adı age2 olsun
# bu değişkenin index değerleri ise age değişkenin değerlerinin karesi olsun
df["Age2"] = df["Age"] ** 2
df["Age3"] = df["Age"] / df["Age2"]

import random
df["rassal"] = [random.randrange(1, 100) for sat in df.index]

df.head()

# değişken silmek istersek tüm stunu axis = 1 geçici ama
df.drop("Age3", axis=1).head()

df.drop("rassal", axis=1,inplace=True)

# bir listeye bağlı olarak değişken silebiliriz.
col_names = ["Age2", "Embarked", "Age3"]

df.drop(col_names, axis=1).head()

df.head()

# Önemli değerli bir bilgi bakın;
# isminde age ifadesi geçen değişkenleri bulalım

#   içerisinde age ifadesi geçenleri seç -->
df.columns.str.contains('Age')
# içerisinde age olmayanları seç
~df.columns.str.contains('Age')

# içerisinde age olmayanları  getir
df.loc[:, ~df.columns.str.contains('Age')].head()

# içerisinde age olanları getir.
df.loc[:, df.columns.str.contains('Age')].head()

# peki bunu comprehension yöntemi ile yaparsak;

# içerisinde age olanları getir.
deneme = [a for a in df.columns if "Age" in a]
type(deneme)

a = df[[abc for abc in df.columns if 'Age' in abc]]
type(a)

# içerisinde age olmayanları getir.
a = df[[abc for abc in df.columns if 'Age' not in abc]]

# age ya da AGE ya da Age yazan olabilir o zaman nasıl yazarız?
df.columns.str.contains("Age|age")

###########BURADA KALDIK
import pandas as pd
df = pd.read_csv(r"G:\Drive'ım\ML\1.datasets\titanic.csv")
df.info()

df["Age2"] = df["Age"] ** 2
df["Age3"] = df["Age"] / df["Age2"]

#######################
# Value'lar Üzerinde İşlemler
#######################

df.values

for row in df.values:
    print(row)
# değerler üzerinde işlemler yapmak istediğimizde

#######################
# iloc & loc
#######################
# daha rahat seçim yapmak için düşünebiliriz.
#
# iloc: integer based selection

df.head()
# 0'dan 3' e kadar seçim yapmak istersem
df.iloc[0:3]
df.iloc[0, 0]

df.iloc[0:3,0:3]

# loc: label based selection
# satırlarda ki ya da sütünlarda ki isimlendirmelere dayanarak seçim yapmamızı sağlar.

df.loc[0:3]
# 4 değer geldi neden çünkü isimlendirmeye göre alım yapıyor öyle olunca 3'ü isim olarak algılıyor

df[0:3]

# 0-3 satırları ve yaş değişkenini getir desem;
# normal yöntem
df[0:3, "Age"]

# iloc ile deneyelim,
df.iloc[0:3, "Age"]

# loc ile deneyelim
df.loc[0:3, "Age"]

# birden fazla değişken seçmek istersem
col_names = ["Age", "Embarked", "Ticket"]

df.loc[0:3, col_names]

#######################
# Koşullu Seçim (Conditional Selection)
#######################

# değişkeni nasıl çağırıyorduk?
df["Age"].head()
df.Age.head()

# birden fazla değişkeni çağırıyoruz
df[["Age", "Age2", "Age3"]].head()

# Yaşı 50' den büyük mü?
df["Age"] > 50

# 50'den büyük olanları getir
df[df["Age"] > 50]

# 50'den büyük kaç kişi var?
df[df["Age"] > 50].count()

# çıktıyı daha düzgün alalım
df[df["Age"] > 50]["PassengerId"].count()

# 50'den büyük olan kişiler kimler?
df[df["Age"] > 50]["Name"]

# bu isimlerden eşsiz olanları getir
df[df["Age"] > 50]["Name"].nunique()

# BUNU LOC İLE yapalım neden e çünkü şartım var ve sütün istiyorum
df.loc[df["Age"] > 50, "Name"].head()

# Yaşı 50'den büyük olan ve cinsiyeti kadın olanları alalım
# DİKKAT birden fazla koşul olduğunda koşullar parantez ile ayrılmalıdır.

df[(df["Age"] > 50) & (df["Sex"] == "female")].head()

df.loc[(df["Age"] > 50) & (df["Sex"] == "female"), "Name"]

# Yaşı 50'den büyük olan kadınların sayısı kaçtır?
df[(df["Age"] > 50) & (df["Sex"] == "female")].count()
df[(df["Age"] > 50) & (df["Sex"] == "female")]["PassengerId"].count()


df[df["Age"] > 50]["PassengerId"].count()

#############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#############################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

# Yaşı 50'den büyük olanların cinsiyetlere göre gruplamasını yapalım

# yaşı 50'den büyük olanlar
df[df["Age"] > 50]["PassengerId"].count()

# yaşı 50'den büyük olanların cinsiyetlere göre hesaplanması
# burada sözlük kullanarak hangi değişkene ne uygulayacağını söyleriz
df[df["Age"] > 50][["PassengerId", "Sex"]].groupby("Sex").agg("count")

# alternatif yol:  aynı işlemi loc ile yapalım

df.loc[df["Age"] > 50, ["PassengerId", "Sex"]].groupby("Sex").agg("count")

# Yaşı 50'den büyük olanların hem sayılarını hemde yaş ortalamalarını hesaplayalım
df.loc[df["Age"] > 50, ["Age", "Sex"]].groupby("Sex").agg(["count", "mean"])

# DİKKAT verilen iki kodu inceleyelim.

df[df["Age"] > 50][["PassengerId", "Sex"]].groupby("Sex").agg({"PassengerId": "count"})

df.loc[df["Age"] > 50, ["Age", "Sex"]].groupby("Sex").agg(["count", "mean"])

# birden fazla fonksiyon(count, mean) kullanıldığında liste içerisinde çağırma eğiliminde olmalıyız.


df.loc[df["Age"] > 50, ["PassengerId", "Age", "Sex"]].groupby("Sex").agg({"PassengerId": "count",
                                                                          "Age": ["min", "max", "mean"]}).head()
# yaşı 50'den büyük olanlar cinsiyete göre gelsin, ve yaşların min max ortalama değerlerini alalım. dict

# şimdi verinin kırılımını arttıralım cinsiyet- embarked liman ve bilet sınıfına göre  yolcuların sayısı,
# aynı sınıfta ki yolcuların yaş ortalaması min max değerini çağıralım

df.loc[df["Age"] > 50].groupby(["Sex", "Embarked", "Pclass"]).agg({"PassengerId": "count",
                                                                   "Age": ["min", "max", "mean"]})

# tüm veriye uygulayalım
df.groupby(["Sex", "Embarked", "Pclass"]).agg({"PassengerId": "count",
                                               "Age": ["min", "max", "mean"]})

# agg fonksiyonun önemli güzelliklerinden
# almak istediğimiz bilgileri bir liste ile belirleyelim;
agg_functions = ["nunique", "first", "last", "sum", "var", "std"]

# bu listeyi al ve yaş değeri üzerinde uygula diyelim.
df.groupby(["Sex", "Embarked", "Pclass"]).agg({"PassengerId": "count",
                                               "Age": agg_functions})

#######################
# Pivot table
#######################

df = pd.read_csv('1.datasets/titanic.csv')


def load_titanic():
    return pd.read_csv('1.datasets/titanic.csv')


df = load_titanic()
df_yedek = df.copy()

# Satırlarda cinsiyet sutunlarda liman bilgisi olsun ve bu bilgilere göre ortalama yaş bilgisini alalım.
df.pivot_table(values="Age", index="Sex", columns="Embarked", aggfunc="min")


#######################
# Sayısal Değişkenin Kategorik Değişkene Çevrilmesi
#######################
df.head()
# Amacımız sayısal bilgiler içeren yaş değişkenini verdiğimiz aralıklarla
# kategorik değişkene dönüştürmek olsun.
# qcut ve cut fonksiyonu bu işlem için kullanılmaktadır.
# qcut çeyreklik değerlerine göre, cut verilen değer aralıklarına göre böler.

df["deneme"] = pd.qcut(df["Age"],q=8).head()
df.drop("deneme", axis=1, inplace=True)

df["new_age"] = pd.cut(df["Age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("Survived", index="Sex", columns="new_age")

df.pivot_table("Survived", index=["Sex", "Pclass"], columns="new_age")


# Hem hayatta kalanların ortalama değerlerini hemde frekansı verelim

df.pivot_table("Survived", aggfunc=["mean","count"], index="Sex", columns="new_age")

#############################################
# Apply ve Lambda
#############################################
# Daha önce şöyle bir şsey yapmıştık
df = load_titanic()

df["Age2"] = df["Age"] ** 2
df["Age3"] = df["Age"] / df["Age2"]


(df["Age"] ** 2).head()
(df["Age2"] ** 2).head()
(df["Age3"] ** 2).head()


for col in df.columns:
    if "Age" in col:
        print(col)

for col in df.columns:
    if "Age" in col:
        print((df[col] ** 2).head())

# yaptığım değişikliği df'e atayayım
for col in df.columns:
    if "Age" in col:
        df[col] = df[col] ** 2

df[["Age", "Age2", "Age3"]].apply(lambda x: x ** 2).head()

# Daha programatik hali tüm satırları ve age içeren sütunları getir ve verilen formülü uygula
df.loc[:, df.columns.str.contains('Age')].apply(lambda x: x ** 2).head()

# daha karmaşık bir fonksiyon uygulayalım normalizasyon işlemi
df.loc[:, df.columns.str.contains('Age')].apply(lambda x: (x - x.mean()) / x.std()).head()

df[["Age"]].apply(lambda x: (x - x.mean()) / x.std()).head()

# Açıklamak için aynı işlemi tekrar yapalım;

# bir fonksiyon tanımlayalım
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

# fonksiyonu deneyelim.
standart_scaler(df["Age"]).head()

# Fonksiyonu apply ile uygulayalım.
# Dikkat apply ile verirken herhangi bir sütun ismi vermedik
# Çünkü apply bu işlemin seçilen sütunlarda olduğunu fonksiyona iletir.
df[["Age"]].apply(standart_scaler).head()

df.loc[:, df.columns.str.contains('Age')].apply(standart_scaler).head()

df.loc[:, df.columns.str.contains('Age')].apply(lambda x: (x - x.mean()) / x.std()).head()

# Atama yapalım bu kadar işlem yaptık
df.loc[:, ["Age", "Age2", "Age3"]] = df.loc[:, df.columns.str.contains('Age')].apply(standart_scaler)


#############################################
# Birleştirme (Join) İşlemleri
#############################################

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df1

df2 = df1 + 99

df2

#######################
# concat ile Birleştirme İşlemleri
#######################

# alt alta birleştirmek
pd.concat([df1, df2])

# indexlerde problem var gibi gözüküyor
pd.concat([df1, df2], ignore_index=True)

# Peki değişken isimleri farklı olsaydı?
df2.columns = ["var1", "var2", "deg3"]
df1.columns

# Birleşen df'te boşluklar olacak.
pd.concat([df1, df2])

# Eğer sadece kesişen isimler ile birleştirme yapmak istersek:
pd.concat([df1, df2], join="inner")

#######################
# Merge ile Birleştirme İşlemleri
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

# Amaç: Her çalışanın işe başlangıç tarihine ulaşmak
pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)

# Amaç: Meslek grubu yeteneklerinin kişilerle eşleştirilmesi
df5 = pd.DataFrame({'group': ['accounting', 'accounting', 'engineering', 'engineering', 'hr', 'hr'],
                    'skills': ['math', 'excel', 'coding', 'linux', 'excel', 'management']})

pd.merge(df1, df5)

