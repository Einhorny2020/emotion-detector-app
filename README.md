# Détecteur d'Émotions IA – Projet Streamlit + DeepFace

Ce projet permet de détecter automatiquement les **émotions d’un visage** à partir d’une image uploadée, en utilisant **DeepFace** (modèle pré-entraîné) et **Streamlit** (interface simple).

## Fonctionnalités

- Upload d’image contenant un visage
- Prédiction automatique des émotions : happy, sad, angry, surprise, etc.
- Affichage du score de chaque émotion
- Interface Streamlit simple et rapide



## Installation

### Sous macOS / Linux

```bash
chmod +x install_env_emotion_mac.sh
./install_env_emotion_mac.sh
source venv/bin/activate
streamlit run app.py
```

### Sous Windows

```bat
install_env_emotion_windows.bat
venv\Scripts\activate
streamlit run app.py
```



## Modèle utilisé

DeepFace (backend par défaut : VGG-Face + OpenCV)



## Structure du projet

```
emotion-detector-app/
├── app.py
├── uploads/
├── install_env_emotion_mac.sh
├── install_env_emotion_windows.bat
└── README.md
```


## Dépendances

- `streamlit`
- `deepface`
- `opencv-python-headless`
- `Pillow`



##  Exemple d’émotions détectées

- happy 😊
- sad 😢
- angry 😠
- surprise 😮
- neutral 😐

