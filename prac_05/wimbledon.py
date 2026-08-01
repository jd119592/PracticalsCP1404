""" Word_occurrences.py
estimated time: 30min
actual time:    35min
Write a program to read this file, process the data and display processed information:

the champions and how many times they have won.
the countries.csv of the champions in alphabetical order
Requirements and Hints
You need to store the data in appropriate data structures.
The solution uses: a list of lists, a dictionary and a set.

The file is not in simple ASCII format but UTF-8 with a byte order mark, or BOM.
You can account for this by setting the encoding like:

with open(filename, "r", encoding="utf-8-sig") as in_file:"""


import csv


def main():
    wimbledon = "wimbledon.csv"
    with open(wimbledon, "r", encoding="utf-8-sig") as in_file:
       name_to_champ_number, new_line, champs = readcsv(in_file)


    print("Wimbledon Champions:")
    for name, number in name_to_champ_number.items():
       print(f"{name}, {number}")
    print()
    print(f"These {len(champs)} countries.csv have won Wimbledon:")
    print(*champs, sep=", ")


def readcsv(in_file):
    name_to_champ_number = {}
    champs: list = []
    new_line = csv.reader(in_file)
    header = next(new_line)
    print(header)
    for row in new_line:
        # print(row)
        if row[2] in name_to_champ_number:
            name_to_champ_number[row[2]] += 1

        else:
            name_to_champ_number[row[2]] = 1
            champs = get_champ_country_list(row, champs)
    return dict(name_to_champ_number), new_line, champs


def get_champ_country_list(row, champs):
     if row[1] not in champs:
        champs.append(row[1])
     return list(champs)

main()