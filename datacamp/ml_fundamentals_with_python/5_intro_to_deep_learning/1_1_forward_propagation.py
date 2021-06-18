import numpy as np


def coding_the_forward_propagation_algorithm():
    weights = {
        'node_0':  np.array([2, 4]),
        'node_1': np.array([4, -5]),
        'output': np.array([2, 7])
    }
    input_data = np.array([3, 5])

    # Calculate node 0 value: node_0_value
    node_0_value = (input_data * weights['node_0']).sum()
    # Calculate node 1 value: node_1_value
    node_1_value = (input_data * weights['node_1']).sum()
    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_value, node_1_value])
    # Calculate output: output
    output = (hidden_layer_outputs * weights['output']).sum()
    # Print output
    print(output)


coding_the_forward_propagation_algorithm()
