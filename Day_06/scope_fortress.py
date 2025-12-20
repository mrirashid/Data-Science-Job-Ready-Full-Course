## create a global variable and change in function
x = 10;

def change_x():
    x = 20;
    return x
change_x() 
print(x) # it prints 10 not 20.
