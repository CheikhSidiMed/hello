animals = {"Cat", "Rabbit", "Camel", "Cow", "Fox"}
animals = set(["Cat", "Rabbit", "Camel", "Cow", "Fox"])
print(animals)
animals1 = {"Lion", "Camel", "Dog", "Cat"}
print(animals | animals1)
print(animals & animals1)
print(animals - animals1)
print(animals ^ animals1)
print("Dog" in animals1)
print("Dog" not in animals1)

data_scientist = {"Python", "R", "SQL", "Git"}
data_ingineer = {"Python", "Java", "Scala", "SQL", "Git", "Hadoop"}
# data_scientist |= {"SAS"}
data_scientist.add("SAS")
print(data_scientist)
print(data_scientist.pop())
data_ingineer.remove("Scala")
data_ingineer.discard("Scala")#remove if in the set
print(len(data_ingineer))
print(data_ingineer & data_scientist)
my_skills = {"Python", "SQL"}
print(my_skills <= data_scientist)

# Exo1
users = {
    "user1": 123123,
    "user2": 700350,
    "user3": 444555
}
name = input("Enter your name: ")
password = int(input("Entre your Password: "))
if name in users.keys() and users[name]==password :
    print("User has been identified")
else :
    print("Username or password does not match")

