## map(func, list)
def map_logic(tranformation_func,data_list):
    for item in data_list:
    new_val=tranformation_func(item)
    yield new_val

    
