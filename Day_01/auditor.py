raw_value=input("Enter a raw value:")
try:
    print(f'You have entered:{raw_value}')
    value=float(raw_value)
    print(f'Converted value is:{value:.2f}')
except ValueError:
    print("Error: Invalid input, cannot convert to float.")
