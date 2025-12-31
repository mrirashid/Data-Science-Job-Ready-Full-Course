# create a list of 10 million numbers
numbers_list = list(range(1, 10000001))

# create a set of the same numbers
numbers_set = set(numbers_list)


# check if -5 exists in set (Hash lookup: O(1))
if -5 in numbers_set:
    print("-5 exists in the set")
else:
    print("-5 does NOT exist in the set")