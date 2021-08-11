
import nltk
from nltk.stem import WordNetLemmatizer
import string
# nltk.download('popular', quiet=True)
import sklearn
import random
import streamlit as st

def para_bot(file):
    file = file.lower()

    sent_tokens = nltk.sent_tokenize(file)
    word_tokens = nltk.word_tokenize(file)

    lemmer = nltk.stem.WordNetLemmatizer()

    def LemTokens(tokens) :
        return [lemmer.lemmatize(token) for token in tokens]

    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemNormalize(text) :
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    def response(user_response) :
        robot_response = ''
        sent_tokens.append(user_response)
        TfidfVec = sklearn.feature_extraction.text.TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = sklearn.metrics.pairwise.cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if (req_tfidf == 0) :
            if user_response == "":
                robot_response = " "
                return robot_response
            else:
                robot_response = robot_response + "idk, This text may not be in your paragraph. Maybe change the question language a lil bit and check your spellings meanwhile ?"
                return robot_response
        else:
            robot_response = robot_response + sent_tokens[idx]
            return robot_response

    greeting_inputs = ['Hello', 'Hi', 'Hey', 'Hiya', 'Hola', 'Namaste']

    def greeting(sentence):

        for word in sentence.split():
            if word.lower() in greeting_inputs :
                return random.choice(greeting_inputs)

    print("Working till sentence")



    flag=True
    st.subheader("Hey ! I'll answer all your questions regarding the text you just entered !")
    st.markdown('<br>', unsafe_allow_html=True)
    if (flag==True):
        a = st.markdown('Enter Question : ')
        user_response = st.text_input('')
        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)

        # print("You : " + user_response)
        user_response=user_response.lower()
        if(user_response!='bye!!'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                st.markdown("Bot: Anytime")
            else:
                if(greeting(user_response)!="" and greeting(user_response)!=None ):
                    st.markdown("Answer : "+greeting(user_response))

                else:
                    st.markdown("Answer : ")
                    st.markdown(response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag=False
            st.text("Bot: take care..")



