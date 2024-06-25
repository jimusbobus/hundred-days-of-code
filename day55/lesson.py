inputs = [1, 2, 3]


# TODO: Create the logging_decorator() function 👇

def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        result = fn(args[0], args[1], args[2])
        print(f"you called {fn.__name__}")
        print(f"It returned: {result}")
        return result

    return wrapper


# TODO: Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a * b * c


z = a_function(inputs[0], inputs[1], inputs[2])

print(z)
