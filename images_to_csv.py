import os
import cv2
import numpy as np
import pandas as pd

# Dossier contenant les images
IMAGE_FOLDER = "images/"
OUTPUT_CSV = "dataset.csv"

# Dictionnaire des étiquettes (formes)
LABELS = {
    "1": "Carre",
    "2": "Triangle",
    "3": "Rectangle",
    "4": "Cercle"
}

# Taille des images (doit correspondre à la taille des images enregistrées)
IMG_SIZE = 64  

data = []
labels = []

# Parcourir toutes les images dans le dossier
for filename in os.listdir(IMAGE_FOLDER):
    if filename.endswith(".png"):
        # Extraire le label depuis le nom du fichier (ex: "1-3.png" → label = 1)
        shape_id = filename.split("-")[0]
        
        if shape_id in LABELS:
            img_path = os.path.join(IMAGE_FOLDER, filename)
            
            # Charger l'image en niveaux de gris
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            if img is not None:
                # Redimensionner au cas où
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                
                # Normaliser les pixels (0 → 1)
                img_flattened = img.flatten() / 255.0
                
                # Ajouter aux données
                data.append(img_flattened)
                labels.append(shape_id)

# Convertir en DataFrame Pandas
df = pd.DataFrame(data)
df.insert(0, "Label", labels)  # Insérer la colonne des labels

# Sauvegarde en CSV
df.to_csv(OUTPUT_CSV, index=False)

print(f"✅ Dataset sauvegardé sous '{OUTPUT_CSV}' avec {len(data)} images !")
