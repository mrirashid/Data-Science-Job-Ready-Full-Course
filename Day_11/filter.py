## remove all negative values from list
def filter_logic(check_func, data_list):
    for item in data_list:
        is_valid = check_func(item)
        if is_valid is True:
            yield item

# Function to remove negative numbers
def is_positive(x):
    return x >= 0

is_positive()

