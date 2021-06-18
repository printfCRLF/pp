import numpy as np
from sklearn.metrics import mean_squared_error


def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)

    # Return the value just calculated
    return(output)


def predict_with_network(input_data_point, weights):
    node_0_input = (input_data_point * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    node_1_input = (input_data_point * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    hidden_layer_values = np.array([node_0_output, node_1_output])
    input_to_final_layer = (hidden_layer_values * weights['output']).sum()
    model_output = relu(input_to_final_layer)

    return(model_output)


def get_slope(input_data, target, weights):
    preds = (input_data * weights).sum()
    error = preds - target
    slope = 2 * input_data * error
    return slope


def get_mse(input_data, target, weights):
    errors = get_error(input_data, target, weights)
    mse = np.mean(errors**2)
    return(mse)


def get_error(input_data, target, weights):
    preds = (weights * input_data).sum()
    error = preds - target
    return(error)
