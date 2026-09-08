#Validate a URL format using basic checks (scheme + domain).
#Example: https://www.google.com -> Valid, google.com -> Invalid (no scheme)

import re
url = input("Enter URL: ")
pattern = r"^https?://.+"
print("Valid URL:" if re.match(pattern, url) else "Invalid URL")