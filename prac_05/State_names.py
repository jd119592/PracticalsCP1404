"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

short_state = input("Enter short state: ")
while short_state != "":
    # try short_statevislower():
    for i in CODE_TO_NAME:
        print(f"{i:4} is {CODE_TO_NAME[i]:4}")

    short_state = short_state.upper()

    # if short_state in CODE_TO_NAME:
    #     print("your pick:",short_state, "is", CODE_TO_NAME[short_state])
    # else:
    #     print("Invalid short state")

    # for short_state in CODE_TO_NAME:
    try:
        print("your pick:", short_state, "is", CODE_TO_NAME[short_state])
    except KeyError:
        print("Invalid short state")



    short_state = input("Enter short state: ")
