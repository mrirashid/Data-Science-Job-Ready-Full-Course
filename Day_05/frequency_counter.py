## Input a string and create a dictionary

input_text='banana' # defined the banana as input

## empty frequency to count characters
frequency={}

for characters in input_text:
    if characters in frequency:
        frequency[characters]+=1
    else:
        frequency[characters]=1
        
        print(f"frequency is {frequency}")


