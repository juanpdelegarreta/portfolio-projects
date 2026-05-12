user_selection = 3
match user_selection:
    case 1:
        print("1 - print all the data")
    case 2:
        print("2 - update the data")
    case 3:
        print("3 - delete the data")
    case 4:
        print("4 - check the health of the system")
    case 5:
        print("5 - test the system")
    case _:
        print("Invalid selection, please try again")