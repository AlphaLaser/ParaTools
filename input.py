import streamlit as st

import chatbot
import summary
import nltk
nltk.download('popular', quiet=True)
import sklearn
import random
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from PIL import Image
from bokeh.models.widgets import Div
import graph
import tts
import text_scrape

url = ('https://github.com/AlphaLaser/para-tools')




m = st.sidebar.markdown("""
<style>
div.stButton > button:first-child {
    width : 95% ;
    align: center;
    border-radius : 10px ;
    height: 100px ;
    
}
</style>
""", unsafe_allow_html=True)

m = st.markdown("""
<style>
    st.form.submit_button{
    
        background-color : blue ;
    
    }
}
</style>
""", unsafe_allow_html=True)
title = st.sidebar.header('Navigator 🧭')
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
#st.sidebar.markdown('<br>', unsafe_allow_html=True)

if st.sidebar.button('What it does and Usage'):
    js = "window.open('https://light-feeling-5c3.notion.site/Usage-Guide-919d7c6ab66d41c981319b9ab8a3a137')"  # New tab or window
    #js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)



if st.sidebar.button('Github'):
    js = "window.open('https://github.com/AlphaLaser/para-tools')"  # New tab or window
    #js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
st.sidebar.markdown('<br>', unsafe_allow_html=True)
st.sidebar.markdown('<br>', unsafe_allow_html=True)
title = st.sidebar.header('Contact Us 📞')
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
#st.sidebar.markdown('<br>', unsafe_allow_html=True)

if st.sidebar.button('E-Mail'):
    js = "window.open('mailto:aditmagotra@gmail.com')"  # New tab or window
    #js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)



if st.sidebar.button('Whatsapp'):
    js = "window.open('https://api.whatsapp.com/send?phone=919958877036')"  # New tab or window
    #js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
logo = Image.open(r'images\logo.png')
st.image(logo)
st.markdown('<hr>', unsafe_allow_html=True)

st.header('Paragraph input')
st.markdown('<br>', unsafe_allow_html=True)


choice = st.radio('', ['Enter Text', 'Get from URL'], key = "31234")
st.markdown('<br>', unsafe_allow_html=True)
is_url = False

if choice == 'Enter Text' :
    with st.form(key='my_form'):
        file = st.text_area('Enter Paragraph :      (Tip : Scroll down after pressing submit 😉) ', height = 350, key="278")
        submit_button = st.form_submit_button(label='Submit')

else:
    with st.form(key='url_form'):
        st.text('Enter a URL or submit Blank for a demo url !')
        myurl = st.text_input('Enter URL', key="278")
        submit_button = st.form_submit_button(label='Submit Form')
        if myurl != "":
            file = text_scrape.get_scraped_text(myurl)
            is_url = True
        else:
            st.text('Using Demo URL as you entered Nothing')
            file = text_scrape.get_scraped_text('https://stribny.name/blog/2020/10/how-to-extract-plain-text-from-an-html-page-in-python/')

if is_url == True :
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.header("Full Text (Extracted from webpage)")
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(file)

if file != "":

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.header("Tools")
    st.markdown('<br>', unsafe_allow_html=True)

    st.subheader("Choose the tool you want to use : ")
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    choice = st.radio('', ['Text to Speech','Summary', 'Paragraph Q/A chatbot', 'Keyword Graph'], key = "312")
    st.markdown('<br>', unsafe_allow_html=True)
    if choice == 'Summary' :
        st.markdown('<hr>', unsafe_allow_html=True)
        st.subheader("Summary Length")
        st.markdown('<br>', unsafe_allow_html=True)
        slider = st.slider('',
                             min_value=10,
                             max_value=90,
                             value=30,
                             step=10,
                             key="1234"
                             )
        st.markdown('<br>', unsafe_allow_html=True)
        st.subheader("I want my summary to be " + str(slider) + " % of my paragraph length" )

        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.header("Summary")
        st.markdown('<br>', unsafe_allow_html=True)
        summary.para_summary(file, slider)



    elif choice == 'Paragraph Q/A chatbot':
        st.markdown('<hr>', unsafe_allow_html=True)
        st.header("Chatbot")
        st.markdown('<br>', unsafe_allow_html=True)

        chatbot.para_bot(file)

    elif choice == "Text to Speech" :
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.header("Paragraph Audio")
        st.markdown('<br>', unsafe_allow_html=True)
        tts.tts(file)

    else:
        st.markdown('<hr>', unsafe_allow_html=True)
        st.header("Keyword Graph")
        st.markdown('<br>', unsafe_allow_html=True)
        st.subheader('Total keywords to plot :')
        st.markdown('<br>', unsafe_allow_html=True)


        graph.plot_graph(file)
