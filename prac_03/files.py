"""OPEN File after user input to
test writing to file techniques"""

# Question 1:
name = input("Please enter name:")
name_file = open("name.txt", "w")
print(name, file=name_file)
name_file.close()


# Question 2:
name_file = open("name.txt", "r")
text_line = name_file.readline()
print(f"Hi {text_line}")
name_file.close()


# Question 3:
with open("numbers.txt", "r") as file:
        number_line1 = file.readline()
        number_line2 = file.readline()
lines_sum = int(number_line1) + int(number_line2)
print(f"sum:{lines_sum}")

# Question 4:

with open("numbers.txt", "r") as sum_file:
        total: int = 0
        while True:
                new_line = sum_file.readline()
                if not new_line:
                        break
                total = int(total) + int(new_line)
        print(f"total sum in numbers.txt: {total}")

