def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper


@log_function_call
def sey_something():
    print("Hello, How are you")


sey_something()
