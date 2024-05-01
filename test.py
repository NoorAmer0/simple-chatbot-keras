import random
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from preprocessing import clean_up_sentence
import keras
import joblib

# loading pickled objects
encoder = joblib.load("pickles/encoder.pkl")
responses = joblib.load("pickles/responses.pkl")
tokenizer = joblib.load("pickles/tokensizer.pkl")
#load model
model = keras.models.load_model('models/store_bot_0.h5')

sequence_max_length = 5


#Just for testing
while True:
    p = input('You : ', )
    p = clean_up_sentence(p)
    p = tokenizer.texts_to_sequences([p])
    p = pad_sequences(p, padding='post', maxlen=sequence_max_length)
    output = model.predict(p)
    output = output.argmax()
    target_tag = encoder.inverse_transform([output])[0]
    print(target_tag)
    print('Noor : ', random.choice(responses[target_tag]))
    if target_tag == "thanks" or target_tag == 'noAnswer':
        break