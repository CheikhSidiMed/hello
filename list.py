names = ["Amed", "Nour", 23, True]
print(names)
print(names[:3])
print(names[1:3])
print(names[::2])
print(names[1::3])
print(names[::-1])

languages = ["PHP", "Ruby", "Swift", "Go", "C++", "JavaScript", "Python"]
print(f"{languages[0]}, {languages[-3]}, {languages[-1]}")
print(languages[:3])
languages[4] = "C#"
print(languages)