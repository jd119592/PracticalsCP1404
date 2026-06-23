"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    # try state_codevislower():
    for i in CODE_TO_NAME:
        print(f"{i:4} is {CODE_TO_NAME[i]:4}")

    state_code = state_code.upper()

    # if state_code in CODE_TO_NAME:
    #     print("your pick:",state_code, "is", CODE_TO_NAME[state_code])
    # else:
    #     print("Invalid short state")

    # for state_code in CODE_TO_NAME:
    try:
        print("your pick:", state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")



    state_code = input("Enter short state: ")
