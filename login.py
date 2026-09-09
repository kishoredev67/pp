def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    return "Invalid Credentials"

print(login("admin", "1234"))
```[cite: 1]