import csv

# name = input("What's your name? ")
# house = input("What's your house? ")

with open("D:\\python programes\\CS50\\file\\exo.csv", "a") as file:
#    write = csv.DictWriter(file, fieldnames=["name", "house"])
#    write.writerow({"name": name, "house": house})
   write = csv.DictReader(file)
   
print(type(write))

