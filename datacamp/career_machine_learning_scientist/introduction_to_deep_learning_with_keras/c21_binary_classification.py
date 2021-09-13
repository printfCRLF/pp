import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from data import load_banknotes_data


def exploring_dollar_bill(banknotes):
    sns.pairplot(banknotes, hue="class")
    plt.show()
    print('Dataset stats: \n', banknotes.describe())
    print('Observations per class: \n', banknotes["class"].value_counts())


def a_binary_classification_model():
    model = Sequential()
    model.add(Dense(1, input_shape=(4,), activation="sigmoid"))
    model.compile(loss='binary_crossentropy', optimizer="sgd", metrics=['accuracy'])
    model.summary()

    return model


def is_this_dollar_bill_fake(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train, epochs=20)
    accuracy = model.evaluate(X_test, y_test)[1]
    print('Accuracy:', accuracy)


if __name__ == "__main__":
    sns.set()
    banknotes = load_banknotes_data()
    exploring_dollar_bill(banknotes)
    features = banknotes.drop(columns=["class"])
    label = banknotes["class"]
    X_train, X_test, y_train, y_test = train_test_split(features, label, stratify=label, test_size=0.25)
    model = a_binary_classification_model()
    is_this_dollar_bill_fake(model, X_train, X_test, y_train, y_test)
