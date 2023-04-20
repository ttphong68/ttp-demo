import gtts
from playsound import playsound
import streamlit as st

# make request to google to get synthesis
tts = gtts.gTTS("Hello world")
# save the audio file
tts.save("hello.mp3")
# play the audio file
playsound("hello.mp3")

# in spanish
tts = gtts.gTTS("Xin chào mọi người", lang="vi")
tts.save("hola.mp3")
playsound("hola.mp3")

# all available languages along with their IETF tag
st.write(gtts.lang.tts_langs())