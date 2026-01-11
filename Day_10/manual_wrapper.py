def my_decorator(original_function):
    def wrapper():
        print("Before Call")
        original_function()
        print("After Call")
    return wrapper
