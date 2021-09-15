import matplotlib.pyplot as plt
from keras.layers import Input, Dense
from keras.models import Model
from keras.utils import plot_model
from sklearn.model_selection import train_test_split
from data import load_games_tourney_data


def build_a_model():
    input_tensor = Input(shape=(1,))
    output_tensor = Dense(1)(input_tensor)
    model = Model(input_tensor, output_tensor)
    model.compile(optimizer="adam", loss="mean_absolute_error")
    return model


def visualize_a_model(model):
    model.summary()
    plot_model(model, to_file='model.png')

    data = plt.imread('model.png')
    plt.imshow(data)
    plt.show()


def train_and_evaluate_a_model(model, games_tourney_train, games_tourney_test):
    model.fit(games_tourney_train["seed_diff"], games_tourney_train["score_diff"],
              epochs=1,
              batch_size=128,
              validation_split=0.1,
              verbose=True)

    X_test = games_tourney_test["seed_diff"]
    y_test = games_tourney_test["score_diff"]
    print(model.evaluate(X_test, y_test, verbose=False))


if __name__ == "__main__":
    model = build_a_model()
    # visualize_a_model(model)


    df = load_games_tourney_data()
    games_tourney_train, games_tourney_test = train_test_split(df, test_size=0.2)
    train_and_evaluate_a_model(model, games_tourney_train, games_tourney_test)
