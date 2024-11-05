import numpy as np
import matplotlib.pyplot as plt 
liste = np.linspace(0, 100, 20)
kareListe = liste ** 2
kupListe = liste ** 3

yeniFigur = plt.figure(figsize=(10, 10),dpi=100)
# size boyutu dpi ise çözünürlüğü belirtir
# dpi sınırları 72 ile 300 arasında olabilir ama ben denedşm 100 iyi
yeniEksen = yeniFigur.add_axes([0.1,0.1,0.9,0.9])
yeniEksen.plot(liste, kareListe, "r*-", label = "Kare")
yeniEksen.plot(liste, kupListe, "y*-", label = "Küp")
yeniEksen.legend(loc = "center left")
plt.show()
# loc seçenekleri : best, upper right, upper left, lower left, 
# lower right, right, center left, center right
# lower center, upper center, 
# dpi ı kaydederken ayarlayabilirsin
# yeniFigur.savefig("yeniFigur.png", dpi = 300)


