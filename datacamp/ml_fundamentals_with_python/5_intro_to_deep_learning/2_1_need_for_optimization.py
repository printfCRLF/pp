import numpy as np
from sklearn.metrics import mean_squared_error
from util import predict_with_network


def changing_weight():
    # The data point you will make a prediction for
    input_data = np.array([0, 3])

    # Sample weights
    weights_0 = {'node_0': [2, 1],
                 'node_1': [1, 2],
                 'output': [1, 1]
                 }

    # The actual target value, used to calculate the error
    target_actual = 3

    # Make prediction using original weights
    model_output_0 = predict_with_network(input_data, weights_0)

    # Calculate error: error_0
    error_0 = model_output_0 - target_actual

    # Create weights that cause the network to make perfect prediction (3): weights_1
    weights_1 = {'node_0': [2, 1],
                 'node_1': [1, 2],
                 'output': [1, 0]
                 }

    # Make prediction using new weights: model_output_1
    model_output_1 = predict_with_network(input_data, weights_1)

    # Calculate error: error_1
    error_1 = model_output_1 - target_actual

    # Print error_0 and error_1
    print(error_0)
    print(error_1)


def errors_for_multiple_data_points():
    input_data = np.array([np.array([0, 3]), np.array([1, 2]),
                           np.array([-1, -2]), np.array([4, 0])])
    target_actuals = np.array([1, 3, 5, 7])
    # Create model_output_0
    model_output_0 = []
    # Create model_output_1
    model_output_1 = []

    weights_0 = {'node_0': [2, 1], 'node_1': [1, 2], 'output': [1, 1]}
    weights_1 = {'node_0': [2, 1], 'node_1': [1, 2], 'output': [1, 0]}

    for row in input_data:
        model_output_0.append(predict_with_network(row, weights_0))
        model_output_1.append(predict_with_network(row, weights_1))

    mse_0 = mean_squared_error(model_output_0, target_actuals)
    mse_1 = mean_squared_error(model_output_1, target_actuals)

    print("Mean squared error with weight_0, %f" % mse_0)
    print("Mean squared error with weight_1, %f" % mse_1)


#changing_weight()
errors_for_multiple_data_points()
