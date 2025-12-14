value=input("Enter a raw number of seconds:")
try:
    print(f'The seconds you entered are: {value}')
    minutes=float(value)/60
    print(f'The minutes are: {minutes:.2f}')
    hours=value//3600
    print(f'The hours are: {hours:.2f}')
except ValueError:
    print("Error: Invalid input")