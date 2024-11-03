import pandas as pd
import numpy as np  

# az önce numpy ile çalıştığım için söylüyorum numpy da arrayler matrixler 
# pandas da ise dataframe ler üzerinde işlem yapılır

# SERİES 

sozluk = {"Ali" : 50, "Veli" : 60, "Ayşe" : 70}
pandasSeries =  pd.Series(sozluk)
# print(pandasSeries)
print(type(pandasSeries))

# bu şekilde bir seri oluşturulabilir data type int olma sebebi ise 
# isimleri index gibi kabul etmesi
isimler = ["Ali", "Veli", "Ayşe"]
yaslar = [50, 60, 70]
pandasSeries = pd.Series(index= isimler,data= yaslar) # isimler index yaslar ise değer olur
print(pandasSeries)# hangisinin index hangisinin değer olduğunu belirtmek önemli

numpyArray = np.array(yaslar)
print(numpyArray)
print(type(numpyArray))
pandasSeries = pd.Series(data= numpyArray, index= isimler) 
print(pandasSeries)
# serilere veri olarak nunpy arrayler de verilebilir
print(f"alinin yaşı: {pandasSeries['Ali']}")

yarismaBir = {"Ali" : 50, "Veli" : 60, "Ayşe" : 70, "osman" : 200 }
yarismaBir = pd.Series(yarismaBir)
yarismaIki = {"Ali" : 55, "Veli" : 65, "Ayşe" : 75}
yarismaIki = pd.Series(yarismaIki)

yarismaSonucu = yarismaBir + yarismaIki
print(yarismaSonucu)
print(type(yarismaSonucu)) # indexi aynı olanlar toplandı diğerleri NaN oldu

# DATAFRAME 