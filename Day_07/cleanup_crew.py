## Write a try/except block that divides two numbers.

try:
        num1=3
        num2=10
        print(f"Dividision of two numbers: {num1/num2}")
except ValueError:
        print("Failed to do divide two nubmers")
except ZeroDivisionError:
        print("Cannot divide zero")
finally:
         print("Excetion completed")
