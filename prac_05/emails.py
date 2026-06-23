""" Word_occurrences.py
estimated time: 30min
actual time:    35min
program that stores users' emails (unique keys) and names (values) in a
dictionary.Remember to use our naming convention for dictionaries,
 key_to_value"""

def main():

    email = input("Email: ")
    name_to_email = {}

    while email != "":
        full_name = extract_name(email)
        user_response = input(f"Is your name {full_name}? (Y/n)")
        if user_response == "Y":
            name_to_email[full_name] = email
        else:
            manual_name = input("Name: ")
            name_to_email[manual_name] = email

        email = input("Email: ")

    print("Finished")
    for name, email in name_to_email.items():
        print(f"{name}  ({email})")


def extract_name(email):
    user_name = email.split('@')[0]
    name_parts = user_name.split('.')
    full_name = " ".join(name_parts)
    return full_name

main()


