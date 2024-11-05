import numpy as np
import matplotlib.pyplot as plt

yasListe = np.random.normal(70, 20, 10)

kiloListe = np.random.normal(70, 20, 10)

plt.plot(yasListe, kiloListe, "b")# sondaki "r" rengi belirtir.
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.title("Yaş-Kilo Grafiği")
# plt.show()
# burdaki verileri ben otomatik oluşturduğum için karışık bir grafik oluştu.

np_liste = np.linspace(0, 100, 20) # 0 ile 100 arasında 100 tane sayı oluşturur.
new_liste = np_liste ** 3
# plt.plot(np_liste, new_liste, "g--") # "--" çizgiyi kesik yapar.
plt.plot(np_liste, new_liste, "g*-") # "*" noktaları belirtir.yılar
plt.xlabel("sayılar")
plt.ylabel("sayıların küpü")
plt.title("Küp Grafiği")
# plt.show()
plt.subplot(1, 2, 1) # 1 satır 2 sütun olacak şekilde 1. grafiği çizdirir.
plt.plot(np_liste, new_liste, "g*-")
plt.subplot(1, 2, 2) # 1 satır 2 sütun olacak şekilde 2. grafiği çizdirir.
plt.plot(new_liste, np_liste, "b--")
# plt.show()

benimFigure = plt.figure()
figureAxis = benimFigure.add_axes([0.2, 0.2, 0.8, 0.8])
# ilk iki değer grafiğin nereden başlayacağını belirtir.
# son iki değer grafiğin ne kadar büyük olacağını belirtir.
figureAxis.plot(np_liste, new_liste, "g--")
figureAxis.set_xlabel("sayilar")
figureAxis.set_ylabel("sayilarin küpü")
figureAxis.set_title("Küp Grafiği")
plt.show()
