import numpy as np
import matplotlib.pyplot as plt

myArray = np.array([1, 2, 3, 4, 5])
# listeden numpy array oluşturmak
print(type(myArray))

# numpy da arrayler üzerinde işlem yapmak çok daha kolaydır.

print(myArray*2)

# matris oluşturma

myMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(myMatrix)

myNumpyMatrix = np.array(myMatrix)
print(myNumpyMatrix)

# arange metodu range metoduna benzer

listem = np.arange(0, 10)
print(listem)

# aynı range gibi son elemaon dahil değil
atlamaliListem = np.arange(0, 10, 2)
print(atlamaliListem)

#zeros metodu
sifirListem = np.zeros(5)
print(sifirListem)

sifirMatrix = np.zeros((4, 4)) # iki boyutlu olursa tuple olarak verilmeli
print(sifirMatrix)


# ones metodu

birListem = np.ones(5)
print(birListem)    

birMatrix = np.ones((4, 4))
print(birMatrix)

# LİNESPACE METODU
# belirli bir aralıkta belirli sayıda eleman oluşturur
# sayılar arasında eşit uzaklık olur

linesSpaceListem = np.linspace(0, 10, 10) 
print(linesSpaceListem)
# 0 ile 10 arasında 10 tane eleman oluşturur    
linesSpaceListem = np.linspace(0,20,5)
print(linesSpaceListem)
# 0 ile 20 arasında 5 tane eleman oluşturur


# EYE METODU birim matris oluşturur

eyeMatrix = np.eye(9)   
print(eyeMatrix)    

# RANDOM METODU rastgele sayılar oluşturur
# default olarak 0 ile 1 arasında sayılar oluşturur
randomListem = np.random.rand(10)
print(randomListem)


randomMatrix = np.random.rand(5, 5)
print(randomMatrix)

kisi_sayisi = 100
for i in range(10):
    deger = np.random.randint(0,kisi_sayisi,15) # 1 ile 100 arasında 15 tane rastgele sayı oluşturur
    if 1 in deger:
        print("1 var") 
    kisi_sayisi -= 1
nurmalSayilar = np.arange(0, 100)
print(nurmalSayilar)



# DİZİ METODLARI 

# RESHAPE METODU

yuzluDizi = np.arange(0, 100)
print(yuzluDizi)

sekilliDizi = yuzluDizi.reshape(10, 10)
print(sekilliDizi)

# MAX VE MİN METODLARI argmax ve argmin metodu ile indexlerine ulaşılabilir

print(sekilliDizi.max())
print(sekilliDizi.argmax())
print(sekilliDizi.min())
print(sekilliDizi.argmin())


# burda sayılar belli olduğu için indexleride belli karışık yapalım

sekilsizDizi = np.random.randint(0, 100, 100)
print(f"shape : {sekilsizDizi.shape}")
sekilsiMatrix = sekilsizDizi.reshape(10, 10)
print(sekilsiMatrix)
print(f"shape : {sekilsiMatrix.shape}")
# shape metodu ile boyutunu öğrenebiliriz
print(sekilsizDizi.max())
print(sekilsizDizi.argmax())
print(sekilsizDizi.min())
print(sekilsizDizi.argmin())


# parçalama işlemleri 

rangeDizi = np.arange(0, 20)
rangeDizi[0:10] = 10
parcaDizi = rangeDizi[0:10]
# parcalanis dizi değişirse asıl dizidede değişim olur önlemek için copy metodu kullanılır

print(parcaDizi)
parcaDizi[:] = 20
print(rangeDizi)

rangeDizi = np.arange(0, 20)
rangeDiziCopy = rangeDizi.copy()

parcaDizi = rangeDiziCopy[0:10]
rangeDiziCopy[0:10] = 10 
print(f"rangeDiziCopy : {rangeDiziCopy}")
print(f"parcaDizi : {rangeDizi}") # parcaDizi değişmedi


# matris işlemleri ve indexleme

matris = np.random.randint(0, 100, 9)
matris = matris.reshape(3, 3)
print(matris)

print(matris[0])
print(matris[0][0])

print(matris[1:,1:]) # 1. satır ve 1. sütundan sonrası yani 2*2 lik matris 
print(matris[1:,1]) # 2. satırdan sonrası için 2. sütün
print(matris[0:,0:]) # direk matrisin kendisi

parcaMatris = matris[[0, 2]] # 0. ve 2. satırı alır
print(parcaMatris)

# OPERASYONLAR

yeniDizi = np.random.randint(0, 100, 20)
print(yeniDizi > 10) # 10 dan büyük olanları true yapar
bigger =  yeniDizi[yeniDizi > 10] # 10 dan büyük olanları getirir
print(bigger)

isBigger = yeniDizi > 50
print(yeniDizi[isBigger]) # 50 den büyük olanları getirir uzun yol gibi

print(yeniDizi)
print(yeniDizi + yeniDizi)
print(yeniDizi * yeniDizi)
print(yeniDizi / yeniDizi) # 0 olanlar 0/0 olduğu için nan olur hata vermez ""