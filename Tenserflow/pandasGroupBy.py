import pandas as pd
import numpy as np

maasSozlugu = {"Departman": ["Yazilim", "Yazilim", "Pazarlama", "Pazarlama", "Hukuk", "Hukuk"],
               "Calisan Ismi": ["Ahmet", "Mehmet", "Ali", "Veli", "Ayse", "Fatma"],
               "Maas": [100, 200, 300, 400, 500, 600]}
# dict ten data frame geçmek gerçekten rahat oluyor bu örneği olsum
maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)
# group by sql ile birebür çalışır
departmanlar = maasDataFrame.groupby("Departman")
print(departmanlar.describe())
print(departmanlar.count())
print(departmanlar.max())
print(departmanlar.min())
print(departmanlar.sample())
# sample rastgele bir değer seçer