import matplotlib.pyplot as plt
import seaborn as sns
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from data import load_banknotes_data


def flow_of_tensors(X_test):
    model = Sequential()
    model.add(Dense(2, input_shape=(4,), activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    inp = model.layers[0].input
    out = model.layers[0].output
    inp_to_out = K.function([inp], [out])
    # print(inp_to_out([X_test]))

    model.compile(loss='binary_crossentropy', optimizer="sgd", metrics=['accuracy'])

    return model, inp_to_out


def neural_separation(model, inp_to_out, X_train, X_test, y_train, y_test):
    for i in range(0, 21):
        # Train model for 1 epoch
        h = model.fit(X_train, y_train, batch_size=16, epochs=1, verbose=0)
        if i % 4 == 0:
            layer_output = inp_to_out([X_test.values])[0]
            test_accuracy = model.evaluate(X_test, y_test)[1]
            plot(layer_output, i, test_accuracy)


def plot(layer_output, i, test_accuracy):
    fig, ax = plt.subplots()
    plt.scatter(layer_output[:, 0], layer_output[:, 1], c=y_test, edgecolors='none')
    plt.title('Epoch: {}, Test Accuracy: {:3.1f} %'.format(i + 1, test_accuracy * 100.0))
    plt.show()


if __name__ == "__main__":
    banknotes = load_banknotes_data()
    features = banknotes.drop(columns=["class"])
    label = banknotes["class"]
    X_train, X_test, y_train, y_test = train_test_split(features, label, stratify=label, test_size=0.25)
    model, inp_to_out = flow_of_tensors(X_test.values)
    neural_separation(model, inp_to_out, X_train, X_test, y_train, y_test)
