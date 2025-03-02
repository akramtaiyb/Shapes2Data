import numpy as np
import matplotlib.pyplot as plt

# Charger le dataset (sans Pandas)
dataset = np.loadtxt("dataset.csv", delimiter=",", skiprows=1)

# Séparer les labels et les images
y = dataset[:, 0].astype(int)  # Première colonne = labels
X = dataset[:, 1:]  # Les pixels des images

# Normaliser les pixels (optionnel : entre 0 et 1)
X = X / 255.0

# Afficher quelques images aléatoires
fig, axes = plt.subplots(2, 5, figsize=(10, 5))  # 2 lignes, 5 colonnes
axes = axes.ravel()  # Aplatir pour un accès facile

for i in range(10):
    idx = np.random.randint(0, len(X))  # Prendre une image aléatoire
    img = X[idx].reshape(64, 64)  # Reformater en 64x64
    axes[i].imshow(img, cmap="gray")  # Afficher en niveaux de gris
    axes[i].set_title(f"Label: {y[idx]}")
    axes[i].axis("off")  # Enlever les axes

plt.show()
