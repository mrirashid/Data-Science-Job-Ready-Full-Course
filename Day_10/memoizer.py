def memoizer(original_function):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = original_function(n)
        return cache[n]
    return wrapper
