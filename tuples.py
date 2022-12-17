# personal_info = ("Cheikh", "cheikh@gmail.com", "27880405")
# print(type(personal_info))
# print(personal_info)
# rgb_colors = tuple(["Red", "Green", "Blue"])
# print(rgb_colors)
import math as m

a = (2, 5)
b = (3, -2)
print(a, b)
print(a + b)
# b[1] = 7 tuple is immutable
# print(b)
distance = m.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
print(f"Distance = {distance:.2f}")
# pour calculer les nombre de paration d'une nombre
print(a.count(2))
print(a.index(2))
print(max(a))
print(len(a))
del b

