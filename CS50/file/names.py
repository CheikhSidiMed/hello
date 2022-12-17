names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")




# lire file


# with open("names.txt", "r") as file:
#     # lines = file.readlines()
#     for line in file:
#         print("helo,", line.rstrip())

# for line in lines:
#     print("helo,", line.rstrip())


# White in file
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# file.close()
