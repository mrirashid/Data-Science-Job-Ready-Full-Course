## ask user for a number. if negative shows a error.
try:
    number=int(input("Enter the number: "))
    if number < 0:
        raise ValueError("No negatives")
    print(f"You have entered: {number}")
except ValueError as e:
    print(e)

