def main():
    height = int(input("Height: "))
    print_column(height)




def print_column(height):
    for i in range(1, height+1):
        print("# " * i)


main()