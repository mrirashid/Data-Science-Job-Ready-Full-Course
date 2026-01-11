def decorator(func):
    def working_wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return working_wrapper
