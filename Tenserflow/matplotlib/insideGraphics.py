import numpy as np  
import matplotlib.pyplot as plt

yasListe = np.linspace(20, 110, 10) 
yas_kup = yasListe ** 3
# figürü oluşturuyoruz.
figure = plt.figure()
# ilk ekseni oluşturdum burda
eksen1 = figure.add_axes([0.1, 0.1, 0.9, 0.9])
eksen1.plot(yasListe, yas_kup, "b*-")
eksen1.set_xlabel("Yaş")
eksen1.set_ylabel("Yaş Küp")
eksen1.set_title("Yaş-Küp Grafiği")
eksen2 = figure.add_axes([0.2, 0.5, 0.3, 0.3])
eksen2.plot(yas_kup, yasListe, "r--")
eksen2.set_xlabel("Yaş Küp")
eksen2.set_ylabel("Yaş")
eksen2.set_title("Yaş-Küp Grafiği")
plt.show()
# burda başlangıç noktalarının önemni anladık eğer aynı figür içinde 
# birden fazla grafik varsa daha anlamlı oluyor
# aynı şekilde devam ederek ikiden fazla eksende oluşturabiliriz

# yukarıda aynı grafik üzerinde iki farklı grafik oluşturduk.
# iki fatklı grafik için önceki gibi subplot kullanıcaz

plt.plot(yasListe, yas_kup, "b*-")
plt.xlabel("Yaş")
plt.ylabel("Yaş Küp")
plt.title("Yaş-Küp Grafiği")
plt.subplot(1, 2, 1)
plt.plot(yasListe, yas_kup, "b*-")
plt.subplot(1, 2, 2)
plt.plot(yas_kup, yasListe, "r--")
plt.show()

# iki grafik iç içe olduğunda kendimiz variable üstünden eksen oluşturup işlem yapıyoruz
# iki farklı grafiği yan yana koymak içinse direk plt üzerinden işlem yapıyoruz



""" (benimFigure, benimEksen) = plt.subplots()
# subplots boş olarak çağrıldığı zaman bi figür ve eksenleri döndürür
# figürü ve eksenleri ayrı ayrı değişkenlere atayabiliriz
# benimFigure.savefig("benimfigur.png", dpi = 200)
benimEksen.plot(yasListe, yas_kup, "g--")
plt.show() """
(benimFigure, benimEksenler) = plt.subplots(nrows=1,ncols=2)
# subplots boş olarak çağrıldığı zaman bi figür ve eksenleri döndürür
# figürü ve eksenleri ayrı ayrı değişkenlere atayabiliriz
# benimFigure.savefig("benimfigur.png", dpi = 200)
print(type(benimEksenler)) # bize aynı tabloda iki farklı eksen döndü

for eksen in benimEksenler:
    eksen.plot(yasListe, yas_kup, "g--")
# benimFigure.savefig("benimfigur.png", dpi = 200)
plt.tight_layout()
print(benimFigure)