# The infinite input pattern
while True:
    pwd=input("set password (min 5 chars):")
    if len(pwd)>=5:
        print("password set")
        break # Exit the loops
    print("Too short! Try again")