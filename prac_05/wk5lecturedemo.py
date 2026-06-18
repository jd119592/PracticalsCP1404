"""Lecture Demo 05 - Dictionaries"""

# name_to_age = {"Billy": 21, "Jan": 34, "Sven": 56}
# for name, age in name_to_age.items():
#     print(f"{name} is {age}")
#
# ages = list(name_to_age.values())
# ages.sort()
# print(ages)
# # for name in name_to_age:
# #     print(f"{name} is {name_to_age[name]}")

# do this now ----------------

# name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
#
# new_name = input("Name: ")
# new_age = int(input("Age: "))
#
# name_to_age[new_name] = new_age
# max_length = max(len(new_name) for name in list(name_to_age.keys()))
# for name, age in name_to_age.items():
#     print(f"{name:{max_length}} - {age:3}")

# sets comprehension --------------------

# [number for number in numbers]
# [3, 1, 4, 1, 5, 9, 2]
# [number * 2 for number in numbers]
# [6, 2, 8, 2, 10, 18, 4]
# [number * 2 for number in numbers if number > 2]
# [6, 8, 10, 18]
# {number for number in numbers if number > 2}
# {9, 3, 4, 5}
# {str(number): number for number in numbers if number > 2}
# {'3': 3, '4': 4, '5': 5, '9': 9}
# {number: number * 2 for number in numbers if number > 2}
# {3: 6, 4: 8, 5: 10, 9: 18}

# using zip to make dictionaries------------------
# names = ['Bill', 'Jane', 'Sven']
# ages = [21, 34, 56]
# zip(names, ages)
# <zip object at 0x0000023CD8CD3E00>
# list(zip(names, ages))
# [('Bill', 21), ('Jane', 34), ('Sven', 56)]
# dict(zip(names, ages))
# {'Bill': 21, 'Jane': 34, 'Sven': 56}