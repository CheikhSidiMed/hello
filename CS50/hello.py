# Ask user for their name
def main1():
    x = int(input("Wha's x? "))
    print("x squared is", square(x))

def square(n):
    # return n * n
    return pow(n, 3)

main1()

def main():
    name = input("What's your name?")
    hello(name)
# function
def hello(to="world"):
    print("hello,", to)
main()
# Remove whitespace from str and Capitalize user's name
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()
# name = name.title()

# Say hello to user
# print(f"hello, {name}")
# z = 1000000
# y = round( 2 / 3, 2)
# print(f"{z:,} : {y}")



# hello(name)
