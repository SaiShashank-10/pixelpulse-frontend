# 🎵 PixelPulse | Visual AI Music Curator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify_API-1ED760?style=for-the-badge&logo=spotify&logoColor=white)
![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow?style=for-the-badge)

> **"Turn your visual memories into mathematically perfect soundtracks."**

PixelPulse is a full-stack AI application that uses **Computer Vision (YOLOv8 + CLIP)** to analyze the sentiment, objects, and lighting of an image, then curates a **Spotify Playlist** that matches the exact "vibe" with 98% accuracy.

---

## 🚀 Live Demo
**👉 [Click Here to Try PixelPulse Live](https://pixelpulse-app-v.streamlit.app/)**
*(Note: Requires a Spotify account to save playlists)*

---

## 🧠 How It Works (The AI Pipeline)

PixelPulse isn't just a random music generator. It uses a **Dual-AI Architecture**:

1.  **👁️ Visual Intelligence (CLIP):**
    * Uses OpenAI's `CLIP-ViT-Base` model to convert the image into a high-dimensional vector.
    * Matches the image against artistic anchors (e.g., *Cyberpunk, Noir, Golden Hour, Melancholic*).
2.  **🚗 Object Detection (YOLOv8):**
    * Detects physical objects (Cars, Gym, Food, People) to contextualize the music.
    * *Example:* A "Sunset" vibe + "Car" detection = *Target: Synthwave/Driving Music*.
3.  **📐 Euclidean Math Scoring:**
    * Calculates a "Vibe Vector" (Energy, Valence, Danceability) based on the AI analysis.
    * Fetches songs and calculates the **Euclidean Distance** between the song's audio features and the image's vibe vector to assign a **Match Percentage** (e.g., 98% Match).

---

## ✨ Key Features

* **🎨 AI Vibe Analysis:** Detects subtle moods like "High Octane," "Serene Nature," or "Urban Noir."
* **🌍 Multi-Cultural Engine:** Automatically mixes **English, Hindi, and Telugu** tracks based on the visual context.
* **📊 Smart Scoring:** Displays a real-time "Match Score" using a Rank Decay algorithm to ensure the top songs are the best fit.
* **🔐 Spotify OAuth 2.0:** Full user authentication allows you to **Save Playlists** directly to your real Spotify library with one click.
* **💎 Glassmorphism UI:** A modern, sleek frontend built with Streamlit and custom CSS.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) | Interactive UI with real-time feedback |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) | High-performance async API |
| **AI Models** | ![OpenAI](https://img.shields.io/badge/OpenAI_CLIP-412991?logo=openai&logoColor=white) ![YOLO](https://img.shields.io/badge/Ultralytics_YOLOv8-00FFFF?logo=ultralytics&logoColor=black) | Visual Sentiment & Object Detection |
| **Data** | ![Spotify](https://img.shields.io/badge/Spotify_Web_API-191414?logo=spotify&logoColor=white) | Audio Analysis & Playlist Management |
| **Deployment** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?logo=huggingface&logoColor=black) | Containerized deployment on HF Spaces |

---

## 📸 Screenshots

| **Input Analysis** | **Curated Playlist** |
|:---:|:---:|
| <img src="https://via.placeholder.com/400x200.png?text=Input+Scan+Example" width="400"> | <img src="https://via.placeholder.com/400x200.png?text=Spotify+Results" width="400"> |
| *Real-time object & vibe detection* | *Ranked results with match %* |

*(Note: Replace the placeholder links above with actual screenshots of your app for maximum impact!)*

---

## 🏃‍♂️ How to Run Locally

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PixelPulse.git](https://github.com/YOUR_USERNAME/PixelPulse.git)
    cd PixelPulse
    ```

2.  **Backend Setup (FastAPI)**
    ```bash
    cd backend
    pip install -r requirements.txt
    # Add your Spotify Credentials in main.py
    uvicorn main:app --reload
    ```

3.  **Frontend Setup (Streamlit)**
    ```bash
    # Open a new terminal
    pip install -r requirements.txt
    streamlit run app.py
    ```

---

## ☁️ Deployment Architecture

* **Frontend:** Hosted on **Streamlit Community Cloud** (Connected to GitHub).
* **Backend:** Dockerized and hosted on **Hugging Face Spaces** (Free Tier CPU Basic).
* **Communication:** REST API via HTTPS.

---

## 🤝 Contact

**Sai Shashank** *Full Stack Developer & AI Enthusiast*
[LinkedIn](https://linkedin.com/in/vakkalanka-sai-shashank) | [GitHub](https://github.com/SaiShashank-10)

---
*Made with Lot's of Coffee ☕ and ❤️* | **Copyright © 2025 Sai Shashank. All rights reserved.**
