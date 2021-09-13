from tensorflow.math import reduce_prod
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential


def text_prediction_with_lstms():
    text = 'it is not the strength of the body but the strength of the spirit it is useless to meet revenge with revenge it will heal nothing even the smallest person can change the course of history all we have to decide is what to do with the time that is given us the burned hand teaches best after that advice about fire goes to the heart'
    words = text.split()
    sentences = []
    for i in range(4, len(words)):
        sentences.append(' '.join(words[i - 4:i]))

    # Instantiate a Tokenizer, then fit it on the sentences
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sentences)
    sequences = tokenizer.texts_to_sequences(sentences)
    print("Sentences: \n {} \n Sequences: \n {}".format(sentences[:5], sequences[:5]))

    return tokenizer


def build_your_lstm_model():
    vocab_size = 44
    model = Sequential()

    # Add an Embedding layer with the right parameters
    model.add(Embedding(input_dim=vocab_size, input_length=3, output_dim=8))

    # Add a 32 unit LSTM layer
    model.add(LSTM(32))

    # Add a hidden Dense layer of 32 units and an output layer of vocab_size with softmax
    model.add(Dense(32, activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    model.summary()

    return model


def predict_text(test_text, model, tokenizer):
    if len(test_text.split()) != 3:
        print('Text input should be 3 words!')
        return False

    test_seq = tokenizer.texts_to_sequences([test_text])
    test_seq = np.array(test_seq)
    pred = model.predict(test_seq).argmax(axis=1)[0]

    return tokenizer.index_word[pred]


if __name__ == "__main__":
    tokenizer = text_prediction_with_lstms()
    model = build_your_lstm_model()
    predict_text('meet revenge with', model, tokenizer)
