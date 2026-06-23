"""produce the following sorted and formatted output
Bob    = 612
Xavier = 80
Chantanelle = 9
Dereck     = 7"""

from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# data.sort(key=itemgetter(1, 0), reverse=True)
data.sort(key=itemgetter(0))
data.sort(key=itemgetter(1), reverse=True)
for name, score in data:
    print(f"{name:11} = {score:3}")



# iterate through strings FINAL EXAM +++++++++++++++++++++

name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
longest_name_length = max([len(name) for name in name_to_score])
#longest_name_length = 11
for name, score in name_to_score.items():
    print(f"{name:{longest_name_length}}, = {score:3}")

#-----------------

"""Write a function that takes a list of strings and returns a dictionary of pairs:
  string: length of string"""

def create_dictionary(strings):
    return {string: len(string) for string in strings}
    # string_to_length = {}
    # for string in strings:
    #     length_of_string = len(string)
    #     string_to_length[string] = length_of_string
    #     return string_to_length
    # {'a':1, 'beeeee': 6, 'see': 3, 'Deez': 4}
print(create_dictionary(['a', 'beeeee', 'see', 'Deez']))