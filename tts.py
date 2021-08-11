from gtts import gTTS
import streamlit as st
import random

# The text that you want to convert to audio
def tts(mytext):

    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome

    rand_string_list = []

    count = 0
    while count <= 10 :
        a = random.randint(0,9)
        rand_string_list.append(str(a))
        count += 1

    rand_string = "".join(rand_string_list)
    myobj.save("audio/" + "welcome.mp3" + str(rand_string))
    file_name = ("audio/" + "welcome.mp3" + str(rand_string))
    # Playing the converted file
    audio_file = open(file_name, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
