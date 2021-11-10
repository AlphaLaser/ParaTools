
import nltk
from nltk.stem import WordNetLemmatizer
import string
# nltk.download('popular', quiet=True)
import sklearn
import random
import streamlit as st

lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None)
                         for punct in string.punctuation)


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def response(user_response, tokens):
    robot_response = ''
    tokens.append(user_response)
    TfidfVec = sklearn.feature_extraction.text.TfidfVectorizer(
        tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(tokens)
    vals = sklearn.metrics.pairwise.cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        if user_response == "":
            robot_response = " "
            return robot_response
        else:
            robot_response = robot_response + \
                "idk, This text may not be in your paragraph. Maybe change the question language a lil bit and check your spellings meanwhile ?"
            return robot_response
    else:
        robot_response = robot_response + tokens[idx]
        return robot_response


def greeting(sentence, inputs):

    for word in sentence.split():
        if word.lower() in inputs:
            return random.choice(inputs)


def para_bot(file):
    file = file.lower()

    sent_tokens = nltk.sent_tokenize(file)

    greeting_inputs = ['Hello', 'Hi', 'Hey', 'Hiya', 'Hola', 'Namaste']

    print("Working till sentence")

    flag = True
    st.subheader(
        "Hey ! I'll answer all your questions regarding the text you just entered !")
    st.markdown('<br>', unsafe_allow_html=True)
    if (flag == True):
        a = st.markdown('Enter Question : ')
        user_response = st.text_input('')
        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)

        # print("You : " + user_response)
        user_response = user_response.lower()
        if(user_response != 'bye!!'):
            if(user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                st.markdown("Bot: Anytime")
            else:
                if(greeting(user_response, greeting_inputs) != "" and greeting(user_response, greeting_inputs) != None):
                    st.markdown(
                        "Answer : "+greeting(user_response, greeting_inputs))

                else:
                    st.markdown("Answer : ")
                    st.markdown(response(user_response, sent_tokens))
                    sent_tokens.remove(user_response)
        else:
            flag = False
            st.text("Bot: take care..")


#para_bot("Your Name is a 2016 Japanese animated romantic fantasy film produced by CoMix Wave Films and released by Toho. It depicts a high school boy in Tokyo and a high school girl in the Japanese countryside who suddenly and inexplicably begin to swap bodies. ")
