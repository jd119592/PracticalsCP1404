"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")
#
while 0 <= score:
    if 90 <= score <= 100:
        print("Excellent")
    elif 50 <= score:
        print("Passable")
    elif 0 <= score:
        print("Bad")
    else:
        print("Invalid score")
    score = float(input("Enter score: "))
print("fin")
