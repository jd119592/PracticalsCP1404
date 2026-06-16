"""a program that asks the user for a filename,
 then prints the number of lines in that file"""



def main():
    just_enter = ""
    user_filename = input("Enter filename (empty to exit): ")
    while user_filename != just_enter:

        sum_lines = count_lines(user_filename)
        print(f"total sum in numbers.txt: {sum_lines}")
        user_filename = input("Enter filename: ")
    print("Done!")


def count_lines(user_filename):
    count = 0
    with open(f"{user_filename}.txt", "r") as user_file:
        while True:
                new_line = user_file.readline()
                if not new_line:
                        break
                count = int(count) + int(new_line)
        return count


main()