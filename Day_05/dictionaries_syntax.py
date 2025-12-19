user = {"id":1,
        "name":"Rashid"
        }
# safe Access (.get)
#return None if key missing , prevent crash
email=user.get("email","NOT FOUND")

#iteration
for key , val in user.email():
    print(f"{key}: {val}")