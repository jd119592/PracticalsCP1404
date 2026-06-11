
# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

name = input("Enter name:")
print("(H)ello\n(G)oodbye\n(Q)uit\n")

user_choice = input()
while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {name}")
    elif user_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    user_choice = input()
print("finished")
