

for i in range(1, 21, 2):
    print(i, end=' ')
print()


"""a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100"""

for j in range(0, 101, 10):
    print(j, end=' ')
print()

"""b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 etc"""

for k in range(20, 0, -1):
    print(k, end=' ')
print()

"""c. print a number of stars.
Ask the user for a number, then print that many stars (*), all on one line"""

number_of_lines = int(input("How many star lines:"))
for h in range(0, number_of_lines + 1):
    print('*' * h)