import pandas as pd
import numpy as np

sozluk1 = {"Isim": ["Ahmet", "Mehmet", "Zeynep", "Atıl"],
              "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
              "Kalori": [100, 200, 300, 400]}
dataFrame1 = pd.DataFrame(sozluk1)
print(dataFrame1)
sozluk2 = {"Isim": ["Osman", "Levent", "Atlas", "Fatma"],    
              "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
              "Kalori": [200, 250, 300, 350]}
dataFrame2 = pd.DataFrame(sozluk2)
print(dataFrame2)
sozluk3 = {"Isim": ["Ayse", "Mahmut", "Duygu", "Nur"],
                "Spor": ["Koşu", "Yüzme", "Badminton", "Tenis"],
                "Kalori": [350, 400, 450, 500]}
dataFrame3 = pd.DataFrame(sozluk3)
print(dataFrame3)

# concat
birlesikFrame = pd.concat([dataFrame1, dataFrame2, dataFrame3])
print(birlesikFrame)
# burda indexler 0,1,2,3,0,1,2,3,0,1,2,3 şeklinde oluştu
# bunu düzeltmek için ignore_index= True yaparız
birlesikFrame = pd.concat([dataFrame1, dataFrame2, dataFrame3]
                          , ignore_index= True)
print(birlesikFrame)
# önceki konularla alakalı örnekler
# birlesikFrame.fillna(value= 0, inplace= True) zaten eksik veri yok
print(birlesikFrame[birlesikFrame["Spor"] == "Koşu"])

sporGruplari = birlesikFrame.groupby("Spor")

print(sporGruplari.describe())

# MERGE İŞLEMİ 

mergeSozluk1 = {"Isim": ["Ahmet", "Mehmet", "Zeynep", "Atıl"],
                "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"]}
mergeDataFrame1 = pd.DataFrame(mergeSozluk1)
print(mergeDataFrame1)
mergeSozluk2 = {"Isim": ["Ahmet", "Mehmet", "Zeynep", "Atıl"],
                "Kalori": [100, 200, 150, 250]}
mergeDataFrame2 = pd.DataFrame(mergeSozluk2)
print(mergeDataFrame2)
# merge işlemi inner join gibi çalışır mesela
# ismi aynı olacak şekilde sporun yanına kaloriyi ekler
mergeDataFrame = pd.merge(mergeDataFrame1, mergeDataFrame2, on= "Isim")
print(mergeDataFrame)
# bunu 1 n formdan 3n forma geçmek gibi düşünebilirsin sql le aynı mantık
# eğer bi tabloda olup diğerinde olmayan bir değer varsa onu almaz
# inner joın copy yapmış adamlar adına merge demiş

