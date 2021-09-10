from tensorflow import constant, Variable
import numpy as np


def defining_data_as_constants():
    credit_numpy = np.array([[2.0000e+00,  1.0000e+00,  2.4000e+01,  3.9130e+03],
                             [2.0000e+00,  2.0000e+00,  2.6000e+01,  2.6820e+03],
                             [2.0000e+00,  2.0000e+00,  3.4000e+01,  2.9239e+04],
                             [2.0000e+00,  2.0000e+00,  3.7000e+01,  3.5650e+03],
                             [3.0000e+00,  1.0000e+00,  4.1000e+01, -1.6450e+03],
                             [2.0000e+00,  1.0000e+00,  4.6000e+01,  4.7929e+04]])
    # Convert the credit_numpy array into a tensorflow constant
    credit_constant = constant(credit_numpy)
    # Print constant datatype
    print('\n The datatype is:', credit_constant.dtype)
    # Print constant shape
    print('\n The shape is:', credit_constant.shape)


def defining_variables():
    # Define the 1-dimensional variable A1
    A1 = Variable([1, 2, 3, 4])
    print('\n A1: ', A1)

    # Convert A1 to a numpy array and assign it to B1
    B1 = A1.numpy()
    print('\n B1: ', B1)


if __name__ == "__main__":
    defining_data_as_constants()
    defining_variables()
