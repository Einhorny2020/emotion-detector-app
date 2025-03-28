#!/bin/bash
echo "Création de l'environnement pour Détecteur d'Émotions (macOS/Linux)"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install streamlit deepface opencv-python-headless Pillow
echo "Environnement prêt. Lancez avec : streamlit run app.py"