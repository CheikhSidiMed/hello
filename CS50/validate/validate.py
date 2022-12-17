import re

email = input("What's your email? ").strip()

# username, domain = email.split("@")

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invaled")