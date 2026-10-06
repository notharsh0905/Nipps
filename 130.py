#Implement a function to check if a string is an IPv4 address.
#An IPv4 address consists of four octets (0-255) separated by dots.
#Example: "192.168.1.1" -> Valid, "256.1.1.1" -> Invalid

import re
ip = input("Enter IP address: ")
pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
print("Valid IPv4 address:" if re.match(pattern, ip) else "Invalid IPv4 address")