import matplotlib.pyplot as plt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import streamlit as st

def plot_graph(text):


    stopwords = list(STOP_WORDS)

    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    tokens = [token.text for token in doc]


    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1


    max_frequency = max(word_frequencies.values(), default = 1)

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    # sentence_tokens = [sent for sent in doc.sents]
    #
    # sentence_score = {}
    #
    # for sent in sentence_tokens:
    #     for word in sent:
    #         if word.text.lower() in word_frequencies.keys():
    #             if sent not in sentence_score.keys():
    #                 sentence_score[sent] = word_frequencies[word.text.lower()]
    #             else:
    #                 sentence_score[sent] += word_frequencies[word.text.lower()]

    total = len(word_frequencies)

    total_args = st.slider('', min_value=1, max_value=total, value = 10, step = 1 )


    labels = []
    sizes = []
    count = 1
    for x, y in word_frequencies.items():
        if count <= total_args:
            labels.append(x)
            sizes.append(y)
            count += 1

    plt.pie(sizes, labels=labels)
    plt.axis('equal')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,  labels=labels)
    ax1.axis('equal')
    plt.show()
    st.markdown('<br>', unsafe_allow_html=True)
    if total_args != 1 :
        st.subheader("I want to plot " + str(total_args) + " of the most used keywords in this paragraph")
    else:
        st.subheader("I want to plot the most used keyword in this paragraph")

    st.markdown('<br>', unsafe_allow_html=True)
    st.pyplot(fig1)
