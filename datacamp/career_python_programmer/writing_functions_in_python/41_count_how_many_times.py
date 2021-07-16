def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@counter
def foo():
    print('calling foo()')


@counter
def bar():
    print("calling bar")


foo()
foo()
print('foo() was called {} times.'.format(foo.count))

bar()
print('bar() was called {} times.'.format(bar.count))
