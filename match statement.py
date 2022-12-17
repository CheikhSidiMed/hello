print("1 Arabic\n2 English\n3 Frensh")
choice = int(input("Chooce a number: "))

match choice :
    case 1 :
        print("mar7aben")
    case 2 :
        print("Hello")
        print("How can we help you")
    case 3 :
        print("Bonjour")
    case _ :
        print("Unsupported language")
