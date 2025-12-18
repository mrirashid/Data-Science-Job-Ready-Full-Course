data=[10,20,30,40,50]

# Slicing (Start: Stop: Step)
subset=data[1:4] # [20,30,40]
reverse=data[::-1]# [50,40,30,20,10]

#list comprehension
# [Action for item in list if condition]
squares=[x**2 for x in data];