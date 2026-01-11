def timer(func):
    def wrapper():
        return func()
    return wrapper

@timer
def process_data():
    print("Processing data")
process_data()
