"""program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45."""
import random
TOTAL_PICKS = []


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    generate_picks(number_of_quick_picks)
    for pick_line in TOTAL_PICKS:
        for i in pick_line:
            print(f"{i:2}", end=" ")
        print()

def generate_picks(number_of_quick_picks):
    for j in range(0, number_of_quick_picks):
        pick_line = []
        while len(pick_line) < 6:
            current_pick = random.randint(1, 45)
            if current_pick not in pick_line:
                pick_line.append(current_pick)
        pick_line.sort()
        TOTAL_PICKS.append(pick_line)



main()