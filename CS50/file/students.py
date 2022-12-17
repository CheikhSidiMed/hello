import csv 

name = input("What's your name? ")
home = input("What's your home? ")

with open("D:\\python programes\\CS50\\file\\students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    # writer = csv.writer(file)
    # writer.writerow([name, home])





















# import csv

# students = []

# with open("D:\\python programes\\CS50\\file\\students.csv") as file:
#     # reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"], "house": row["house"]})

    # for line in file:
    #     name, home = line.rstrip().split(",")
    #     student = {}
    #     student["name"] = name
    #     student["home"] = home
    #     students.append(student)
# students.append(f"{name} is in {house}")
# def get_name(student): llambda student: student["name"]
#     return student["name"]


# for student in sorted(students, reverse=True, key=lambda s: s["name"]):
#     print(f"{student['name']} is from {student['home']}")

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
