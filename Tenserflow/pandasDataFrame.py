# DATAFRAME PANDAS
import pandas as pd 
import numpy as np  

matris = np.random.randn(4,3)
dataFrame = pd.DataFrame(matris)
print(dataFrame)
print(dataFrame[0]) # numpy da sıra alırken burda sütun alıyor
print(type(dataFrame)) 
print(type(dataFrame[0])) # sütunlar serilerden oluşur

# index ve column isimlerini belirleyebiliriz

yeniDataFrame = pd.DataFrame(data= matris, index= ["Ali", "Veli", "Ayşe", "Fatma"], columns= ["maas", "yas", "calisma saati"])
print(yeniDataFrame)
print(yeniDataFrame["maas"]) # sütun ismi ile sütun seçme
print(yeniDataFrame[["maas","yas"]]) # birden fazla sütun seçme

# Column seçme
print(yeniDataFrame.loc["Ali"])
# index seçme
print(yeniDataFrame.iloc[0])
# bizim belirlediğimiz indexi kullanabliriz aynı zamanda 1,2,3 gibi indexleride kullanabiliriz

#column eklme

yeniDataFrame["emeklilik"] = yeniDataFrame["yas"] - yeniDataFrame["calisma saati"]
print(yeniDataFrame)

# column silme
yeniDataFrame.drop("emeklilik",axis= 1, inplace= True)
# inplace True olursa kalıcı olur
print(yeniDataFrame)
# axis 0 satır 1 sütun belirtir
# defaultta axis 0 dır column silmek istersen 1 seç
print(yeniDataFrame[yeniDataFrame["maas"] > 0])
# maası 0 dan büyük olanları seçer
# sql deki where gibi düşünebiliriz
print(yeniDataFrame[(yeniDataFrame["yas"] > 0)])

print(yeniDataFrame.reset_index())
# isimler artık index değil column name dönüşür

yeniDataFrame["yeni index"] = ["a", "b", "c", "d"]
print(yeniDataFrame)
print(yeniDataFrame.set_index("yeni index"))
# eski indexler kayboldu bu duruma dikkat et 


# multi index

ilkIndex = ["Simpson", "Simpson", "Simpson", "South Park", "South Park", "South Park"]
icIndex = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]
birlesmisIndex = list(zip(ilkIndex, icIndex))
birlesmisIndex = pd.MultiIndex.from_tuples(birlesmisIndex)
print(birlesmisIndex)
cizgiFilm = pd.DataFrame(np.random.randn(6,2), index= birlesmisIndex, columns= ["yas", "maas"])
print(cizgiFilm)
print(cizgiFilm.loc["Simpson"]) 
print(cizgiFilm.loc["Simpson"].loc["Homer"])
print(cizgiFilm.loc["South Park"])

# index isimlendirme 
cizgiFilm.index.names = ["Film", "Isim"]
print(cizgiFilm)