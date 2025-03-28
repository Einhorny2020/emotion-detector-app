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

```bash si erreur streamlit
### Etre sous Python3.10 minimum

brew install python@3.10
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install streamlit
pip install opencv-python-headless
brew install libjpeg libtiff little-cms2 openjpeg webp
pip install Pillow
pip install tensorflow
pip install keras
pip install deepface

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

