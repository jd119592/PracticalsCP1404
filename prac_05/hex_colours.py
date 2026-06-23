"""return colour code from name of colour in input"""

COLOUR_TO_CODE = {"absolute zero": "0048ba", "acid green": "b0bf1a", "aliceblue": "f0f8ff",
                "alizarin crimson": "e32636", "amaranth": "e52b50",
                "amber": "ffbf00", "amethyst": "9966cc", "antiquewhite": "faebd7"}
print(COLOUR_TO_CODE)

short_state = input("Enter colour name: ")
while short_state != "":
    # try short_statevislower():
    for i in COLOUR_TO_CODE:
        print(f"{i:4} is {COLOUR_TO_CODE[i]:4}")

    short_state = short_state.lower()


    # if short_state in CODE_TO_NAME:
    #     print("your pick:",short_state, "is", CODE_TO_NAME[short_state])
    # else:
    #     print("Invalid short state")

    # for short_state in CODE_TO_NAME:
    try:
        print("your pick:", short_state, "is", COLOUR_TO_CODE[short_state])
    except KeyError:
        print("Invalid colour name")



    short_state = input("Enter colour name: ")
