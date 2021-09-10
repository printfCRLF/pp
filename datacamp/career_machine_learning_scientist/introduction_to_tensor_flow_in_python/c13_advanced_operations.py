from tensorflow import reshape, Variable, GradientTape, multiply, matmul, reduce_sum
from tensorflow.python.framework.constant_op import constant


def reshaping_tensors(gray_tensor, color_tensor):
    # Reshape the grayscale image tensor into a vector
    gray_vector = reshape(gray_tensor, (28*28, 1))
    # Reshape the color image tensor into a vector
    color_vector = reshape(color_tensor, (28*28*3, 1))


def compute_gradient(x0):
    # Define x as a variable with an initial value of x0
    x = Variable(x0)
    with GradientTape() as tape:
        tape.watch(x)
    # Define y using the multiply operation
        y = multiply(x, x)
    # Return the gradient of y with respect to x
    return tape.gradient(y, x).numpy()


def optimize_with_gradients():
    # Compute and print gradients at x = -1, 1, and 0
    print(compute_gradient(-1.0))
    print(compute_gradient(1.0))
    print(compute_gradient(0.0))


def working_with_image_data():
    model = constant([[1, 0, -1]])
    letter = constant([
        [1, 0, 1],
        [1, 1, 0],
        [1, 0, 1]
    ])

    # Reshape model from a 1x3 to a 3x1 tensor
    model = reshape(model, (3, 1))
    # Multiply letter by model
    output = matmul(letter, model)
    # Sum over output and print prediction using the numpy method
    prediction = reduce_sum(output)
    print(prediction.numpy())


if __name__ == "__main__":
    optimize_with_gradients()
    working_with_image_data()
