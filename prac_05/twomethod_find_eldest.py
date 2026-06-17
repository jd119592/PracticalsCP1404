"""The function will return the name of the oldest person in the list.
If multiple people have the same oldest age, return the first name."""

# def main():
#     names = ["ash", "jed", "will"]
#     ages = [20, 20, 18]
#     eldest_name = find_oldest(names, ages)
#     print(eldest_name)
#
# def find_oldest(names, ages):
#     eldest = max(ages)
#     for i in range(len(ages)):
#          if eldest == ages[i]:
#              return names[i]
#              # return eldest_name
#
# main()

# -------------------

def find_oldest(names2, ages2):
    #return names2[ages2.index(max(ages2))]
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages2):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names2[oldest_index]



def run_tests():
    i = 0
    names2 = ["Bill", "Jane", "Sven"]
    ages2 = [21, 34, 56]
    # print(names2[i], "is", ages2[i], "years old")
    print(find_oldest(names2, ages2))
run_tests()