import pandas as pd
import numpy as np

# elimize eksik veri olduğu durumlarda yapmamız gerekenler
data = np.random.randint(0, 30, (4,4)).astype("float")
# aklında bulunsun int değerler non olarak atanamaz 
sehirAdlari = ["Ankara", "İstanbul", "İzmir", "Antalya"]
günler = ["Pazartesi", "Sali", "Çarşamba", "Perşembe"]
havaDurumu = pd.DataFrame(data = data,index= sehirAdlari, columns= günler)
print(havaDurumu)

# şu an elimizde eksik veri yok olduğu bir senaryoda
# öncelikle veri olmasa bile dataFrame oluştururken hata almayız örneğin

data[0, 0] = np.nan
data[1, 2] = np.nan
data[2, 1] = np.nan
data[2, 2] = np.nan
eksikFrame = pd.DataFrame(data = data, index= sehirAdlari, columns= günler)
print(eksikFrame)

# non verş olanları yok etme
print(eksikFrame.dropna())
# non olmayan kolonları seçne
print(eksikFrame.dropna(axis= 1)) 
# içinde n tane değer olan sütunlar korunur
print(eksikFrame)
print(eksikFrame.dropna(thresh=3))

# boi yerlere default değer atama

eksikFrame.fillna(value= 20, inplace= True)
print(eksikFrame)