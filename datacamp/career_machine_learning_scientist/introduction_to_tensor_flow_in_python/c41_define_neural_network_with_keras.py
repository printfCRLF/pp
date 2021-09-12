from tensorflow import keras


def the_sequential_model_in_keras():
    model = keras.Sequential()
    model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))
    model.add(keras.layers.Dense(8, activation="relu"))
    model.add(keras.layers.Dense(4, activation="softmax"))
    print(model.summary())


def compiling_a_sequential_model():
    model = keras.Sequential()
    model.add(keras.layers.Dense(16, activation="sigmoid", input_shape=(784,)))
    model.add(keras.layers.Dropout(0.25))
    model.add(keras.layers.Dense(4, activation="softmax"))
    model.compile('adam', loss='categorical_crossentropy')
    print(model.summary())


def defining_a_multiple_input_model(m1_inputs, m2_inputs):
    # For model 1, pass the input layer to layer 1 and layer 1 to layer 2
    m1_layer1 = keras.layers.Dense(12, activation='sigmoid')(m1_inputs)
    m1_layer2 = keras.layers.Dense(4, activation='softmax')(m1_layer1)

    # For model 2, pass the input layer to layer 1 and layer 1 to layer 2
    m2_layer1 = keras.layers.Dense(12, activation='relu')(m2_inputs)
    m2_layer2 = keras.layers.Dense(4, activation='softmax')(m2_layer1)

    # Merge model outputs and define a functional model
    merged = keras.layers.add([m1_layer2, m2_layer2])
    model = keras.Model(inputs=[m1_inputs, m2_inputs], outputs=merged)

    # Print a model summary
    print(model.summary())
