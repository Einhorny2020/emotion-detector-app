@echo off
echo Création de l'environnement pour Détecteur d'Émotions (Windows)
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install streamlit deepface opencv-python-headless Pillow
echo Prêt à l'emploi. Lancez : streamlit run app.py
pause