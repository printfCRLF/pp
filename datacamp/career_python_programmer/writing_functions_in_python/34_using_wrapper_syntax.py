from util import print_args


def my_function(a, b, c):
    print(a, b, c)


my_wrapped_function = print_args(my_function)
my_wrapped_function(1, 2, 3)
