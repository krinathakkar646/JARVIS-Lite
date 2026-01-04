import streamlit as st
import speech_recognition as sr
import pyttsx3
import os
import certifi
import time
from google import genai
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# --- 1. SETUP & CONFIGURATION ---
st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="centered")

# Fix SSL & Audio Drivers
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# 🚨 PASTE YOUR API KEY HERE
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

# Initialize Chat History if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 2. THE SAME POWERFUL FUNCTIONS (Backend) ---

def speak(text):
    """Speaks the text using the local computer speakers"""
    try:
        # Re-initialize engine every time to avoid freezing
        engine = pyttsx3.init(driverName='sapi5')
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.warning(f"Audio Output Error: {e}")

def record_audio(duration=5, fs=44100):
    """Records audio for a fixed time (Same as your terminal script)"""
    try:
        # Record
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait for recording to finish
        
        # Safety pause to release driver
        time.sleep(0.5)
        
        # Convert to 16-bit integer
        myrecording_int16 = (myrecording * 32767).astype(np.int16)
        write('chat_input.wav', fs, myrecording_int16)
        return 'chat_input.wav'
    except Exception as e:
        st.error(f"Mic Error: {e}")
        return None

def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return None
    except Exception as e:
        return None

def ask_brain(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=text + " (Keep answer conversational and short, max 2 sentences.)"
        )
        return response.text
    except Exception as e:
        return "I am having trouble connecting to the network."

# --- 3. THE MODERN CHAT UI ---

st.title("🤖 JARVIS AI")
st.caption("Listening on Local Microphone • Powered by Gemini")

# A. Display Chat History
# This loop draws all previous messages every time the app updates
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# B. The Input Area (Bottom of screen)
st.divider()
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # This button acts just like your "Enter" key
    if st.button("🎙️ Tap to Speak (5s)", use_container_width=True):
        
        # 1. Listen
        with st.spinner("🎧 Listening..."):
            filename = record_audio(duration=5)
        
        # 2. Transcribe
        if filename:
            user_text = transcribe_audio(filename)
            
            if user_text:
                # Add User Message to History
                st.session_state.messages.append({"role": "user", "content": user_text})
                with st.chat_message("user"):
                    st.markdown(user_text)

                # 3. Think
                with st.spinner("🤖 Thinking..."):
                    response_text = ask_brain(user_text)

                # 4. Respond (Text + Audio)
                # Add AI Message to History
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                with st.chat_message("assistant"):
                    st.markdown(response_text)
                
                # Speak the answer
                speak(response_text)
                
            else:
                st.warning("❌ I didn't catch that. Try again.")
