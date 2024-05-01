import random
import joblib
import keras
from preprocessing import clean_up_sentence
from keras.preprocessing.sequence import pad_sequences
from flask import Flask, render_template, request

# loading pickled objects
encoder = joblib.load("pickles/encoder.pkl")
responses = joblib.load("pickles/responses.pkl")
tokenizer = joblib.load("pickles/tokensizer.pkl")
#load model
model = keras.models.load_model('models/store_bot_0.h5')

sequence_max_length = 5




app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    text = clean_up_sentence(text)
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text, padding='post', maxlen=sequence_max_length)
    output = model.predict(text)
    output = output.argmax()
    target_tag = encoder.inverse_transform([output])[0]
    return random.choice(responses[target_tag])


if __name__ == '__main__':
    app.run()
