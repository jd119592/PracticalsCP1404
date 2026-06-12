"""
CP1404/CP5632 - Practical
Program to determine score status
"""
# from unittest import result


def main():
    score = float(input("Enter score: "))
    result = process_score(score)
    print(f"Your results are!: {result}")

def process_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()

