name = input("Enter name:")
print("(H)ello\n(G)oodbye\n(Q)uit\n")

def main ():

    user_choice = input()
    while user_choice != "Q":
        process_input(user_choice)
        print("(H)ello\n(G)oodbye\n(Q)uit\n")
        user_choice = input()


def process_input(user_choice: str):
    if user_choice == "H":
        print(f"Hello {name}")
    elif user_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("invalid choice")


print("finished")

main()
