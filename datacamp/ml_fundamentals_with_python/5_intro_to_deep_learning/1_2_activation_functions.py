import numpy as np
from util import relu


def the_rectified_activation_function():
    weights = {
        'node_0':  np.array([2, 4]),
        'node_1': np.array([4, -5]),
        'output': np.array([2, 7])
    }
    input_data = np.array([3, 5])

    # Calculate node 0 value: node_0_output
    node_0_input = (input_data * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value: node_1_output
    node_1_input = (input_data * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output (do not apply relu)
    model_output = (hidden_layer_outputs * weights['output']).sum()

    # Print model output
    print(model_output)


# Define predict_with_network()
def predict_with_network(input_data_row, weights):    # Calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)

    # Return model output
    return(model_output)


def applying_the_network_to_many_obeservations():
    weights = {
        'node_0':  np.array([2, 4]),
        'node_1': np.array([4, -5]),
        'output': np.array([2, 7])
    }
    input_data = np.array([
        np.array([3, 5]), np.array([1, -1]),
        np.array([0, 0]), np.array([8, 4])]
    )

    # Create empty list to store prediction results
    results = []
    for input_data_row in input_data:
        # Append prediction to results
        results.append(predict_with_network(input_data_row, weights))

    # Print results
    print(results)


the_rectified_activation_function()
applying_the_network_to_many_obeservations()
