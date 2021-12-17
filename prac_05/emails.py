"""
CP1404/CP5632 Practical 
Email to name dictionary
"""

def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name(email):  
    prefix= email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()


