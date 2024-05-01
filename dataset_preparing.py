import json
import joblib
import pandas as pd

with open('data/intents.json',encoding="utf8") as json_data:
    data = json.load(json_data)

target = []
val = []
responses = {}
for intent in data['intents']:
    responses[intent['tag']] = intent['responses']
    for pattren in intent['patterns']:
        val.append(pattren)
        target.append(intent['tag'])

dataset = pd.DataFrame({'input':val, 'target':target})

joblib.dump(responses, "pickles/responses.pkl") #the bot will use them
dataset.to_csv('data/dataset.csv')


