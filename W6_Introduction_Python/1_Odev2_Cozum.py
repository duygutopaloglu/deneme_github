"""
Soru 1: Bir öğrencinin vize ve final notları verildiğinde geçiş notunu hesaplayan bir fonksiyon tanımlayınız.
Geçiş puanın hesaplamasında vizenin %40’ını final notunun %60’ını dikkate alınız.
Geçiş notunun hesaplanmasında verilen tabloyu kullanınız.
Başarı
Notu	Başarı
Puanı	Başarı
Notu Katsayı	Sonuç
A1	95-100	4.00	Geçer Not
A2	90-94	3.75
A3	85-89	3.50
B1	80-84	3.25
B2	75-79	3.00
B3	70-74	2.75
C1	65-69	2.50
C2	60-64	2.25
D1	55-59	2.00	Koşullu Geçer
D2	50-54	1.75
F1	0-49	0.00	Başarısız
F2	Devamsız	0.00
"""


def hesapla(mexam=0, fexam=0):
    """
    Hesapla fonksyionu vize ve final notu verilen öğrencinin
    başarı notunu ve başarı puanını hesaplamaktadır.
    Parameters
    ----------
    mexam: Öğrencinin vize sınavında aldığı notu ifade etmektedir.
    fexam: Öğrencinin final sınavında aldığı notu ifade etmektedir.

    Returns
    -------
    point: öğrencinin başarı puanını ifade etmektedir.
            Hesaplama esnasında vize*0,4 + final*0,6 formülü kullanılır.
            Çıkan sonuç yukarı yuvarlanır.
    result: öğrencinin başarı notunu ifade etmektedir.

    """

    point = round((mexam * 0.4 + fexam * 0.6))
    allresult = []
    if point <= 49:
        result = "F1"
    elif point <= 54:
        result = "D2"
    elif point <= 59:
        result = "D1"
    elif point <= 64:
        result = "C2"
    elif point <= 69:
        result = "C1"
    elif point <= 74:
        result = "B3"
    elif point <= 79:
        result = "B2"
    elif point <= 84:
        result = "B1"
    elif point <= 89:
        result = "A3"
    elif point <= 94:
        result = "A2"
    else:
        result = "A1"
    allresult = [mexam, fexam, point, result]
    return allresult


hesapla(95, 95)

"""
Soru 2: 
    1-Fizik dersini alan 10 öğrenci için, vize ve final notlarını rassal olarak oluşturunuz. 
    Oluşturduğunuz notlar için geçiş notlarını hesaplayınız. Her bir öğrencinin vize, final, başarı puanı ve 
    başarı notlarını bir çıktı olarak yazdırınız. 
    Örnek: Ayşe’nin vize 80 final 90 olsun. 
    Bu durumda geçiş puanı = (80*40/100) +(90*60/100) = 86 geçiş notu A3 olacaktır. 

"""
# öğrenci listesini rassal olarak python oluştursun istersek;
# not: siz kendiniz rassal oluştrabilirdiniz elbette bu kısım ekstra bilgi :)


import random

# rassal rakam çağırmak için random kütüphanesini import ettik.
numberofstudent = 10
# Öğrenci sayısını dinamik tutmak için bir değişken oluşturduk.

students = {}
# öğrencilerin numara ve sınav bilgilerini tutmak için boş sözlük oluşturduk.

for student in range(numberofstudent):
    number = random.randrange(1, 10 ** 9)
    exams = [random.randrange(100), random.randrange(100)]
    students.update({number: exams})
print(students)


# öğrencilerin vize ve final notu bilgisine göre başarı puanı, başarı notunu hesaplayan
# ve sonuçları yazdıran fonksiyon yazalım

def classcalculate(students):
    for std in students:
        exams = students[std]
        students.update({std: hesapla(exams[0], exams[1])})
    print(students)


classcalculate(students)

"""
    2- Bir öğrenci numarası verildiğinde bu öğrencinin fizik dersini alıp almadığını sorgulayan bir fonksiyon yazınız. 
    Öğrenci dersi alıyorsa bu öğrencinin not durumunu yazdırınız. 
    Diğer durumda girilen öğrenci bu dersi almamaktadır çıktısını yazdırınız. 
    Örnek: Ekranda olmasını beklediğimiz çıktı: 
    Öğrenci dersi alıyorsa “Ayşe vize 80, final 90, başarı puanı 86 başarı notu A3” şeklinde, 
    öğrenci dersi almıyorsa “191663001 numaralı öğrenci bu dersi almamaktadır.” şeklindedir.

"""


def checkstudent(number):
    if number in students.keys():
        templist = students[number]
        print(f"{number} numaralı öğrencinin vize notu:{templist[0]},"
              f"final notu: {templist[1]}, başarı puanı: {templist[2]}, başarı notu {templist[3]}")
    else:
        print(f"{number}'lı öğrenci fizik dersini almamaktadır.")

checkstudent(309518439)

"""
Soru 3
    1-	car_crashes veri setini çağırınız.
    2-	Veri setinde ki değişkenlerin(Sütunların) isimlerini büyütünüz.
    3-	Veri setinde bulunan nümerik değişkenlerin isimlerini büyütünüz.
    4-	Nümerik değişkenlerin isminin başına "NUM_" ekleyiniz.
    5-	İsminde no ifadesi bulunmayan değişkenlerin sonuna "_FLAG" ekleyiniz ve büyütünüz. Diğer değişkenleri ise büyütünüz. Beklenen çıktı aşağıda verilen şekildedir. 
    ['TOTAL_FLAG', 'SPEEDING_FLAG', 'ALCOHOL_FLAG', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM_FLAG', 'INS_LOSSES_FLAG', 'ABBREV_FLAG']
    6-	Verilen dataframede bulunan "abbrev", "no_previous" değişkenlerini içermeyen yeni bir dataframe oluşturunuz.

"""


# 1- car_crashes veri setini çağırınız.

import numpy as np
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

# 2- Veri setinde ki değişkenlerin(Sütunların) isimlerini büyütünüz.

[col.upper() for col in df.columns]

# 3- Veri setinde bulunan nümerik değişkenlerin isimlerini büyütünüz.
[col.upper() for col in df.columns if df[col].dtype != "O"]
#ya da
[col.upper() for col in df.columns if col in df.select_dtypes([np.number]).columns]

# 4- Nümerik değişkenlerin isminin başına "NUM_" ekleyiniz.
["NUM_"+col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

["NUM_"+col.upper() if col in df.select_dtypes([np.number]).columns else col.upper() for col in df.columns]

# 5- İsminde "no" bulundurmayan değişkenleri belirleyiniz.
[col for col in df.columns if "no" not in col]

# 6- İsminde no ifadesi bulunmayan değişkenlerin sonuna "_FLAG" ekleyiniz ve büyütünüz. Diğer değişkenleri ise büyütünüz.
# Beklenen çıktı;
# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

[col.upper() if "no" in col else col.upper()+"_FLAG" for col in df.columns]

# 7- Verilen dataframede bulunan "abbrev", "no_previous" değişkenlerini içermeyen
# yeni bir dataframe oluşturunuz.

olmasin = ["abbrev", "no_previous"]
new_df = df[[col for col in df.columns if col not in olmasin]]
