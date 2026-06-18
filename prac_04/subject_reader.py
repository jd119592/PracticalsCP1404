"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)

    display_subjects(data)
    subject_to_data = conver_data(data)
    print(subject_to_data)
    subject = input("What subject code: ")
    print(f"{subject_to_data[subject][0]} teaches {subject}")

# def print_subj_details(data):
#     for i in range(0,len(data)):
#         print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")

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
    # print(data_nest)
    return data_nest

def conver_data(data):
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]
    return subject_to_data

def display_subjects(data):
    for subject_data in data:
       # print(f"{data[subject_data][0]} is taught by {data[subject_data][1]} and has {data[data_nest][2]} students")
       print("{} is taught by {:12} and has {:3} students".format(*subject_data))

main()