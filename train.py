import pandas as pd
import joblib
import keras
from sklearn.calibration import LabelEncoder
from preprocessing import clean_up_sentence
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras import layers, Sequential
from keras.layers import Embedding

data = pd.read_csv('data/dataset.csv',encoding='utf8') #Read dataset
data = data.sample(frac = 1) #shuffle dataframe
encoder = LabelEncoder() #label encoding 
tokenizer = Tokenizer()  #tokenize input
sequence_max_length = 5 



data['input'] =  data['input'].apply(clean_up_sentence) #clean

tokenizer.fit_on_texts(data['input'])  #fit tokenizer
encoder.fit(data['target']) #fit encoder

joblib.dump(tokenizer, "pickles/tokensizer.pkl") #save tokenizer
joblib.dump(encoder, "pickles/encoder.pkl") #save encoder


X_val = tokenizer.texts_to_sequences(data['input']) #Tokenize the input
X_val = pad_sequences(X_val, padding='post', maxlen=sequence_max_length) #Padding the input


Y_val = encoder.transform(data['target']) #encode the output

vocab_size = len(tokenizer.word_index) + 1 # +1, for the padding value
classes_num = encoder.classes_.shape[0]


# Build neural network
model = Sequential(
    [   
        keras.Input(shape=(sequence_max_length,)),
        Embedding(vocab_size, 10),
        layers.Dense(8, activation="relu"),
        layers.Flatten(),   #reduce the dimntion for the output layer
        layers.Dense(classes_num, activation="softmax"),
    ]
)

print(model.summary())


#sparse_categorical_crossentropy, because the output is range of integrts
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = model.fit(X_val,Y_val, epochs=300)

model.save('models/store_bot_0.h5')