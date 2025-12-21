## Write a script that asks the user for the age.
while True:
    try:
        age=int(input("Enter you age: "))
        print (f"You have entered the age: {age}")
        break
    except ValueError:
        print("Text is not allowed")