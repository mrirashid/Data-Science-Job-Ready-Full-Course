## reduce collapses a list into a sinle value
def reduce_logic(func, data_list):
    accumulator = data_list[0]
    
    for i in range(1, len(data_list)):
        current = data_list[i]
        accumulator = func(accumulator, current)
    
    return accumulator

def multiply(a, b):
    return a * b

nums = [1, 2, 3, 4]

print(reduce_logic(multiply, nums))
