## check if a value exist in a list
## pseudo code logic

def contains(lst, target):
    index = 0
    length = len(lst)

    while index < length:
        current_value = lst[index]  # access value at this index

        if current_value == target:
            return True             # found match

        index += 1                  # move to next slot

    return False                    # reached end without match
