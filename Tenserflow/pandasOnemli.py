import numpy as np 
import pandas as pd 

maasSozlugu = {"Departman": ["Yazilim", "Yazilim", "Pazarlama", "Pazarlama", "Hukuk", "Hukuk"],
                "Calisan Ismi": ["Ahmet", "Mehmet", "Ali", "Veli", "Ayse", "Fatma"],
                "Maas": [100, 200, 300, 400, 500, 600]}
maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)

# unıque değerler
print(maasDataFrame["Departman"].unique())
# kaç tane unique değer var için nunique yani number of unique
print(maasDataFrame["Departman"].nunique())

print(maasDataFrame)
""" maasDataFrame["Maas"] = maasDataFrame["Maas"] * 7 / 5
print(maasDataFrame) """

# yada fonksiyonlar uygulanabilir

def taxedSalary(salary):
    return salary * 0.7

maasDataFrame["Maas"] = maasDataFrame["Maas"].apply(taxedSalary)
print(maasDataFrame)    

yeniBirVeri = {"karakter sinifi": ["South Park", "South Park", "Simpson", "Simpson", "Simpson"],
                "karakter ismi": ["Cartman", "Kenny", "Homer", "Bart", "Bart"],
                "yas": [9, 10, 50, 20, 10]}

yeniDataFrame = pd.DataFrame(yeniBirVeri)   
print(yeniDataFrame)

# pivot table default ta aynı değerlerin value lerinin ortalamasını alır
pivot_table_default = yeniDataFrame.pivot_table(values= "yas", index= ["karakter sinifi", "karakter ismi"])
print(pivot_table_default)
# en sonda aggfunc ile hangi işlemin uygulanmasını istediğimizi belirtebiliriz
pivot_table_sum = yeniDataFrame.pivot_table(values= "yas", index= ["karakter sinifi", "karakter ismi"], aggfunc= np.sum)
print(pivot_table_sum)
