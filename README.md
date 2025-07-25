
# 💧 Identification of Underground Water Quality Using ML Algorithm

This project predicts the quality of underground water using machine learning, based on simulated sensor data (pH, turbidity, and conductivity). The goal is to determine whether the water is **safe ("Good")** or **unsafe ("Poor")** for usage.

---

## 📌 Project Overview

- Generates realistic water sensor data (pH, turbidity, conductivity)
- Trains a Random Forest model on labeled data
- Uses a Streamlit-based web interface for real-time prediction
- Provides a binary output: **Good** or **Poor** quality

---

## 🚀 Live Web App Demo (Streamlit)

The app interface collects user input and returns a water quality prediction using a pre-trained ML model.

```bash
streamlit run app.py

