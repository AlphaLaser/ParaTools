import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import streamlit as st



def para_summary(text, text_len):

    sum_len = text_len/100

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

    sentence_tokens = [sent for sent in doc.sents]

    sentence_score = {}

    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_score[sent] += word_frequencies[word.text.lower()]



    select_length = int(len(sentence_tokens)*sum_len)


    summary = nlargest(select_length, sentence_score, key=sentence_score.get)

    final_summary = [word.text for word in summary]

    counter = 1

    for i in final_summary :
        st.markdown(str(counter)+ ". " + i)
        counter += 1


