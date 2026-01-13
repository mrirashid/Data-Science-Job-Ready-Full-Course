
def sort_with_key(list, key_func):
    shadow=[]
    for item in list:
        sort_val=key_func(item)
        shadow.append((sort_val,item))
    shadow.sort()
    return [item for sort_val,item in shadow]

data = ["100px", "20px", "3px"]

def extract_number(x):
    return int(x[:-2])   # remove "px"

print(sort_with_key(data, extract_number))
