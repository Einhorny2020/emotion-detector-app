import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np
import os
import uuid

os.makedirs("uploads", exist_ok=True)

st.set_page_config(page_title="Détecteur d'Émotions", layout="centered")
st.title("Détecteur d’Émotions sur une Image")

uploaded_file = st.file_uploader("📷 Importez une image (visage)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    file_path = os.path.join("uploads", f"{uuid.uuid4()}.jpg")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    image = Image.open(file_path)
    st.image(image, caption="Image téléchargée", use_container_width=True)

    with st.spinner(" Analyse des émotions en cours..."):
        try:
            result = DeepFace.analyze(img_path=file_path, actions=['emotion'], enforce_detection=True)
            st.success("Émotion détectée")

            emotion = result[0]['dominant_emotion']
            st.subheader(f"Émotion dominante : {emotion}")

            st.write(" Détails des scores :")
            st.json(result[0]['emotion'])

        except Exception as e:
            st.error(f"Erreur : {str(e)}")