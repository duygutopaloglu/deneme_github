# MATPLOTLIB
#############################################

import matplotlib.pyplot as plt


#############################################
# Kategorik Değişken Görselleştirme
#############################################
import numpy as np
import pandas as pd

def load_titanic():
    return pd.read_csv(r"G:\Drive'ım\ML\1.datasets\titanic.csv")

df = load_titanic()

df['Sex'].value_counts().plot(kind='bar', rot=0)
plt.show()


#############################################
# Sayısal Değişken Görselleştirme
#############################################
import seaborn as sns
df = sns.load_dataset("tips")

# Histogram
plt.hist(df["total_bill"])
plt.show()

# Boxplot
plt.boxplot(df["total_bill"])
plt.show()



#############################################
# Matplotlib'in Özellikleri
#############################################

#######################
# plot
#######################

# İki nokta arasında çizgi çizmek
x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

# Çizgisiz sadece noktaları göstermek
plt.plot(x, y, 'o')
plt.show()

# Daha fazla sayıda nokta
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

#######################
# marker
#######################

y = np.array([13, 28, 11, 100])

# y noktalarına içi dolu daire koymak
plt.plot(y, marker='o')
plt.show()

# y noktalarına yıldız koymak
plt.plot(y, marker='*')
plt.show()

# bu markerlerdan birçok var.
markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

for marker in markers:
    plt.plot(y, marker)
    plt.show()

#######################
# line
#######################

y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show()

# birçok çizgi çeşidi de var
styles = ['dotted', 'dashed', 'dashdot']
for style in styles:
    plt.plot(y, linestyle=style)
    plt.show()

# e birçok renk de var
# hem rengi hem de stilleri değiştirerek yazdıralım
# ve hatta patronu çıldırtalım.
styles = ['dotted', 'dashed', 'dashdot']
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']

for style in styles:
    for color in colors:
        plt.plot(y, linestyle=style, color=color)
        plt.title(style + " " + color)
        plt.show()

# şimdi daha da çıldırtalım patronu
# ihtiyacımız şu olsun.
# biz sözlük var.
# key'lerinde arguman değeri olabilecek stringler value'larında da bu argumanların tanımları olsun.

colors_dict = {'r': "red", 'g': "green", 'b': "blue", 'c': "cyan",
               'm': "magenta", 'y': "yellow", 'k': "black", 'w': "white"}

for style in styles:
    for color in colors_dict.keys():
        plt.plot(y, linestyle=style, color=color)
        plt.title(style.upper() + " " + colors_dict[color])
        plt.show()

#######################
# Multiple Lines
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

#######################
# Labels
#######################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

# Başlık
plt.title("Bu ana başlık")
# X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")
# Y eksenini isimlendirme
plt.ylabel("Y ekseni isimlendirmesi")
# Izgara
plt.grid()

plt.show()

#######################
# Subplots
#######################


# 2 farklı grafiği tek satır iki sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)

plt.show()

# 3 grafiği bir satır 3 sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()

#############################################
# SEABORN
#############################################

# Kategorik Değişkenler: countplot
# Sayısal Değişkenler: histogram ve boxplot

import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")

df.describe().T


#############################################
# Kategorik Değişken Görselleştirme
#############################################

df["sex"].value_counts()

sns.countplot(x=df["sex"], data=df)
plt.show()




#############################################
# Sayısal Değişken Görselleştirme
#############################################

# pandas ile histogram
df["total_bill"].hist()
plt.show()

# seaborn ile boxplot
sns.boxplot(x=df["total_bill"])
plt.show()






