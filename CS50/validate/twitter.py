import re

url = input("URL: ").strip()

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")
matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"Username:", matches.group(1))
