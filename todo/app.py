todos = []


def todo():
    menu()


def menu():
    option = 0
    while option != 4:

        print("Choose an option:")
        print("1.- Add a task")
        print("2.- Show tasks")
        print("3.- Delete a task")
        print("4.- Exit app")
        option = int(input())
        match option:
            case 1:
                print("Please add a task.")

            case 2:
                print("You are seeing the list.")

            case 3:
                print("You deleted a task.")

            case 4:
                print("Exit app.")

            case _:
                print("That's an invalid option.")
