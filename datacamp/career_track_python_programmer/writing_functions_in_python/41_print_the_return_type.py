def print_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("{} returned type {}".format( type(result)))
        return result
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({"bar": "barz"}))
