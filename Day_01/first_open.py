#standard input
# age = input("age:") <-- Returns "25" (string)

#the academy standard (safe)
raw_val=input("Enter Principal:")
try:
    principal=float(raw_val) # Explicit casting
    print(f"Accepted: $ {principal:.2f}") # F-sring formatting
except ValueError:
    print("Error: Invalid input for principal amount.")