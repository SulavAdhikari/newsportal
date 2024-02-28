import numpy as np, pandas as pd, tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from Lemmatization.lemmatizer import NepaliLemmatizer
import pickle
from tensorflow.keras.models import load_model

lem = NepaliLemmatizer()

def lemmatize_nep(text):
    results = lem.hybrid_method(text) 
    ret_val = " ".join([result['lemma'] for result in results[0]])
    return ret_val




model = load_model('deeplearning/sentimentmodel.h5')
label_encoder = pickle.load(open('deeplearning/classes.pk1', 'rb'))
train_data = pickle.load(open('deeplearning/words.pk1', 'rb'))

tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(train_data)

vocab_length = len(tokenizer.word_index) + 1
maxlen = 1000



lang = 'N'


def predict_text(text):
   

    if lang == 'N':
        lemmatized_text = lemmatize_nep(text)
    elif lang == 'E':
        lemmatized_text = lemmatize_eng(text)

    text_sequence = tokenizer.texts_to_sequences([lemmatized_text])
    padded_sequence = pad_sequences(text_sequence, maxlen=maxlen, padding='post', truncating='post')
    # Make prediction
    prediction = model.predict(padded_sequence)

    # Convert prediction to class label
    a = prediction.argmax(axis=1)
    predicted_label = label_encoder.classes_[a] 
    

    return predicted_label

