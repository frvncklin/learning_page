def decorator_parameters(param=None):
    def decorator(func):
        print("Decorator codename: [{}]".format(param))
        def your_new_function(*args, **kwargs):
            result = func(*args, **kwargs)
            final = '{} [{}]'.format(result, param)
            return final
        return your_new_function
    return decorator

@decorator_parameters(90210)
@decorator_parameters(90125)
def sum(x, y):
    return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)