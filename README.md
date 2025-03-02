# 🖌️ Programme de Dessin avec OpenCV

## 📜 Instructions

### 🎯 Objectif

Dessinez et enregistrez 10 dessins pour chaque type de forme.

### 🔧 Commandes

- **Sélectionner une forme** :
  - `1` → Carré
  - `2` → Triangle
  - `3` → Rectangle
  - `4` → Cercle
- **Dessiner** : Maintenez le **clic gauche** et déplacez la souris.
- **Enregistrer un dessin** : Appuyez sur `S` (l’image est sauvegardée en `64x64`).
- **Réinitialiser la toile** : Appuyez sur `R`.
- **Quitter** : Appuyez sur `Q`.

### 🎲 Particularité

- L'épaisseur du trait change **aléatoirement** après chaque sauvegarde.

## 📁 Sauvegarde

- Les dessins sont enregistrés dans `images/` sous le format :

Exemple : `images/1-3.png` → 3ème dessin de type **Carré**.

## 🚀 Exécution

1. Installez les dépendances si nécessaire :

```bash
pip install -r requirements.txt
```

2. Lancer :

```bash
python draw.py
```

3. Créer la dataset :

```bash
python images_to_csv.py
```
