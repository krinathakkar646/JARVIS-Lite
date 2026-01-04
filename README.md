# 🎙️ JARVIS Lite: Voice-Activated AI Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini%202.5-magenta?logo=google&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit&logoColor=white)

A fully functional **Voice-to-Voice AI Assistant** that runs locally. 
Unlike standard chatbots, this project processes raw audio streams, converts speech to text, thinks using **Google's Gemini 2.5 Flash**, and speaks back using a Text-to-Speech (TTS) engine.

## 🚀 Features
- **👂 Hands-Free Interaction:** Uses `SoundDevice` and `NumPy` to capture raw audio without driver crashes.
- **🧠 Advanced Intelligence:** Powered by Google's **Gemini 2.5 Flash** (Sub-second latency).
- **🗣️ Natural Voice Output:** Integrated `pyttsx3` for offline text-to-speech synthesis.
- **💻 Modern UI:** Built with **Streamlit** for a chat-like web interface.
- **⚡ Local-First:** Runs entirely on your machine (Microphone/Speaker hardware access).

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| **LLM Brain** | Google Gemini 2.5 Flash (via `google-genai`) |
| **Speech-to-Text** | `SpeechRecognition` (Google API) |
| **Audio Capture** | `SoundDevice` + `NumPy` (Custom Buffer) |
| **Text-to-Speech** | `pyttsx3` (SAPI5/NCAA Drivers) |
| **Frontend** | Streamlit |

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone [https://github.com/krinathakkar646/JARVIS-Lite.git](https://github.com/krinathakkar646/JARVIS-Lite.git)
   cd JARVIS-Lite

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set up API Key Create a .streamlit/secrets.toml file or export your key:**
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"

▶️ Usage
**Run the Streamlit app:**
```bash
streamlit run jarvis.py
