counter = 1
while counter < 10 :
    print(counter)
    counter += 2
else :
    print("Done")

i = 1
# some_note = 0.0
# note = 0.0
# while note >= 0.0 :
#     some_note += note
#     note = float(input(f"Enter note {i}: "))
#     i += 1
# print(f"Some note {some_note}")
names = []
name = input(f"Enter name {i}: ")
while name != "quit" :
    names.append(name)
    name = input(f"Enter name {i}: ")
    i +=1
print(sorted(names))
j = 0
while j < i-1 :
    print(names[j])
    j += 1


