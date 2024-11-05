import numpy as np
import matplotlib.pyplot as plt

liste = np.linspace(0, 100, 30)
kareListe = liste ** 2
kupListe = liste ** 3


figure = plt.figure(figsize=(10, 10), dpi=100)
eksen = figure.add_axes([0.1, 0.1, 0.9, 0.9])

eksen.plot(liste, kareListe, color ="#FF0000", label = "Kare",alpha = 1,linewidth = 5)
eksen.plot(liste, kupListe, color ="#0000FF", label = "Küp",alpha = 0.5,linewidth = 2,linestyle = "-.")
plt.show()
# linestyle çizgi stilini belirtir seçenekler: - , -- , -., :
# şimdi renklerde red green yerine hex kodları kullanabiliriz
# alpha ise saydamlığı belirtir 1 den 0 a saydamlık artar
# linewidth ise çizginin kalınlığını belirtir
