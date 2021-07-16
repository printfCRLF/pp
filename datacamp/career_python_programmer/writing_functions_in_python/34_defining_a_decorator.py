def print_before_and_after(func):
    def wrapper(*args):
        print("Before {}".format(func.__name__))
        func(*args)
        print("After {}".format(func.__name__))

    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


multiply(1, 5)
