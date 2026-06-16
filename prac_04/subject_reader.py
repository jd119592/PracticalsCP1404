"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)

    print_subj_details(data)

def print_subj_details(data):
    for i in range(0,len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")

def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_nest = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        data_nest.append(data)
        print(data) # See if that worked
        print("----------")
    input_file.close()
    print(data_nest)
    return data_nest

main()