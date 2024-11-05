import numpy as np
import matplotlib.pyplot as plt

liste = np.linspace(0, 100, 20)
kareListe = liste ** 2


# scatter plot 
# figür oluurup eksen ayarlamaya gerek yok bunda 
plt.scatter(liste, kareListe)
plt.show()

# histogram
random_dizi = np.random.randint(0, 100, 50)
plt.hist(random_dizi,50)
plt.show()