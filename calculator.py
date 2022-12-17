n1 = float(input("n1: "))
n2 = float(input("n2: "))
op = input("op: ")


if op == '+' :
    result = n1 + n2
elif op == '/' :
    if n2 == 0 :
        result = "Errer on ne pas divise par 0 "
    else :
        result = n1 / n2
elif op == '-' :
    result = n1 - n2
elif op == '*' :
    result = n1 * n2
else :
    result = "Unknown operator"

    print(result)