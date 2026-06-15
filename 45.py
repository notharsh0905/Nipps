import re

email = "nitish24singh@gmail.com"
match = re.match(r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$', email)
if match:
    username = match.group(1)
    print(username)  # Output: nitish24singh
else:
    print("Invalid email format")   