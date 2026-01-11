def decorator(original_function):
    def wrapper(*args, **kwargs):
        print("Logging...")
        return original_function(*args, **kwargs)
    return wrapper
