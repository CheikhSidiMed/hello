import math
import random as r

print(abs(-3.8))
print(round(3.4))
print(round(3.5))
print(round(3.6))
print(min(7, -2, 10))
print(max(7, -2, 10))
print(math.ceil(3.4))
print(math.floor(3.4))
print(math.sqrt(36))
print(math.pow(3, 4))
print("Le pgsd: ", math.gcd(8, 4))

print("\t********************* ")

print(r.random())
print(r.uniform(1, 10))
print(r.randint(1, 10))#pour int

print("\t Exo: ")
x = float(input("x: ")) 
y = math.pow(3, x/2)
print("y = ", y)
y = abs(math.cos(x) - 4)
print("y = ", y)
z = float(input("entre Z suprieur ou egale 1: "))
y = (7 * x + 2) / math.sqrt(2 * z - 1)
print("y = ", y)
