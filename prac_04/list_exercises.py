"""program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program then outputs information about these numbers"""
# from audioop import avg

numbers = []
print("Give 5 numbers")

for i in range(0, 5):
    number_added = int(input(f"Number: "))
    numbers.append(number_added)
    # print(numbers)

first_number = numbers[0]
last_number = numbers[4]
smallest_number = min(numbers)
largest_number = max(numbers)
avg_number = sum(numbers)/len(numbers)
print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"the average of the numbers is {avg_number}")