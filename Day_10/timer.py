import time

def timer(original_function):
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = original_function(*args, **kwargs)   # Run the logic
        end_time = time.perf_counter()
        print(end_time - start_time)
        return result
    return timer_wrapper
