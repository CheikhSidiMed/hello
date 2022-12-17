# for number in range(1, 8, 2) :
    # print(f"hi {number}")
# text = "Python"
# for char in text :
#     print(char.upper())
# names = ["Sami", "Nour", "Ali", "Zied", "Farah"]
# for name in names :
#     print(name)

# x = int(input("Enter un entier : "))
# for j in range(1, 11) :
#     print(f"{x} x {j} =", x*j)
# students = {
#     "Bilel": 87,
#     "Zied": 45,
#     "Nour": 69,
#     "Omar": 93,
#     "Sara": 56
# }
# for name in students :
#     if students[name] >= 60 :
#         print(name, ":", students[name])
# for name, avarage in students.items() :
#     if avarage >= 60 :
#         print(name, ":", avarage)
menu = {
    "Pizza": 10,
    "Hamburger": 5,
    "Chicken": 8,
    "Shawarma": 7,
    "Fries": 1.5
}
print("    MENU")
for name, priece in menu.items() :
    print(name, ":", priece, "$")
totale_price = 0.0
order_fini = {}
nomber_dorder = int(input("Enter nomber dorder : "))
for n in range(1, nomber_dorder + 1) :
    order = input(f"Enter order {n}: ")
    qty = int(input(f"Enter quantity {n}: "))
    totale_price = totale_price + menu[order] * qty
    order_fini[order] = qty
print("\t","*** Your Order ***")
for nam, priec in order_fini.items() :
    print(" \t*",nam, ":", priec, " \t*")
print(f" \t* total : {totale_price}  $*")

