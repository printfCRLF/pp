from tensorflow import constant, Variable
from tensorflow import ones_like, multiply, matmul, reduce_sum


def performing_element_wise_multiplication():
    # Define tensors A1 and A23 as constants
    A1 = constant([1, 2, 3, 4])
    A23 = constant([[1, 2, 3], [1, 6, 4]])

    # Define B1 and B23 to have the correct shape
    B1 = ones_like(A1)
    B23 = ones_like(A23)

    # Perform element-wise multiplication
    C1 = multiply(A1, B1)
    C23 = multiply(A23, B23)

    # Print the tensors C1 and C23
    print('\n C1: {}'.format(C1.numpy()))
    print('\n C23: {}'.format(C23.numpy()))


def making_prediction_with_matrix_multiplication():
    # Define features, params, and bill as constants
    features = constant([[2, 24], [2, 26], [2, 57], [1, 37]])
    params = constant([[1000], [150]])
    bill = constant([[3913], [2682], [8617], [64400]])

    # Compute billpred using features and params
    billpred = matmul(features, params)

    # Compute and print the error
    error = bill - billpred
    print(error.numpy())


def summing_over_tensor_dimensions():
    wealth = constant([[11, 50], [7, 2], [4, 60],
                       [3, 0], [25, 10]])
    total_wealth = reduce_sum(wealth)
    print("total wealth is ", total_wealth)

    bonds_vs_stocks = reduce_sum(wealth, axis=0)
    print("bonds vs stocks ", bonds_vs_stocks)

    wealth_by_individuals = reduce_sum(wealth, axis=1)
    print("wealth by individuals ", wealth_by_individuals)


if __name__ == "__main__":
    # performing_element_wise_multiplication()
    # making_prediction_with_matrix_multiplication()
    summing_over_tensor_dimensions()
