## create a list of 1 million numbers
numbers_list =list( range(1,1000001)); ## created list of 1 million

# create a set of the same numbers
numbers_set=set(numbers_list)

# check if -1 exists in list
if -1 in numbers_list:
    print("−1 exists in the list")
else:
    print("−1 does NOT exist in the list")

# check if -1 exists in set
if -1 in numbers_set:
    print("−1 exists in the set")
else:
    print("−1 does NOT exist in the set")