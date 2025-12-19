## create a dictionary to access user email
user={"id":1, "name":"Rashidul"}

email=user.get("email","email not found"); ## to access the email 

## check the access
for key, value in user.items():
    print(f"The key is {key} and the value is {value} ")