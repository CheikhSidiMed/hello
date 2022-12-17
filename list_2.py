# l1 = ["Python"]
# print(type(l1))
# l2 = list("Python")
# print(type(l2))
# print(l1,l2)
# number = list(range(1, 21 ))
# print(number)
# print(l1 + l2)
# print(l1 * 2)
# print("Python" not in l1)
# print("Python" in l1)
# l1.append("Java")
# l1.extend(["C#", "C++"])
# l1.insert(0, "CSS")
# print(l1)
# print("Java" in l1)
#remove
# l1.pop(1)
# print(l1)
# l1.pop()
# print(l1)
# l1.remove("C#")
# print(l1)
# del l1[0:2]
# print(l1)
# l1.clear()
# print(l1)
# if "CSS" in l1 :
#    print(l1.index("CSS"))
# else :
#    print("CSS not in the l1")
# print(l1.count("CSS"))

# number = [21, 3, 6, 34, 65, 9, 1, 20]
# print(number)
# number.reverse()
# print(number)
# number.sort()#pour sorter de manier croisante
# print(number)
# number.sort(reverse= True)#pour sorter de manier decroisante
# print(number)
# number_1 = number.copy()
# number_1.append(12)
# print(number_1)
# print(len(number))
# print(min(number))
# print(max(number))

#Exo 
# players = ["Bilel", "Karim", "Wafa", "Omar"]
# print(players)
# print(len(players))
# players.append("Farah")
# players.remove("Karim")
# players.insert(players.index("Wafa"), "Ahmed")
# print(players.index("Omar"))
# players.sort()
# print(players)

student = ["Mohamed", [75, 80, 93]]
student_mark = (student[1][0] + student[1][1] + student[1][2] * 2 ) / 4
print(f"Name\t Mark\n{student[0]}\t {student_mark}")