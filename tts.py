from gtts import gTTS
import streamlit as st

# The text that you want to convert to audio
def tts(mytext):

    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("audio/welcome.mp3")

    # Playing the converted file
    audio_file = open('audio/welcome.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
