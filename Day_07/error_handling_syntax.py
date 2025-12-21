## Error handling ( Exceptions ) 
while True:
    try:
        val=int(input("Enter number: "))
        print(val/100)
        break
    except ValueError:
        print("text is not allowed")
    except ZeroDivisionError: 
        print("Cannot divide by zero")
