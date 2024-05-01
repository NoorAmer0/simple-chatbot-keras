import re
from nltk.stem.isri import ISRIStemmer

st = ISRIStemmer()

def clean_up_sentence(sentence):
    #remove punctuations
    sentence = str(sentence)
    sentence = re.sub(r'[^\w\s]','',sentence)
    #stemming
    stemmed = st.stem(sentence)
    return stemmed

