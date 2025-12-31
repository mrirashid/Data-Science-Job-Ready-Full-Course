# create a list of 10 million numbers
numbers_list = list(range(1, 10000001))

# create a set of the same numbers
numbers_set = set(numbers_list)

# check if -5 exists in list (Linear Scan: O(N))
if -5 in numbers_list:
    print("-5 exists in the list")
else:
    print("-5 does NOT exist in the list")


