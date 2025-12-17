# Ask the user for the password repeatedly
while True:
    pwd=input("Type anything :" )
    if pwd =="stop":
        print("loop stopped")
        break;  # It will stop the loop immediately.
    else:
        print(f"You have typed: {pwd}");
