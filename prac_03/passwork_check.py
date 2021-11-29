'''
CP1404 - Practical 3
Password Check
'''

PASSWORD_MINIMUM_LENGTH=8
PASSWORD_MAXIMUM_LENGTH=16

def version_1():
    password=input("Enter a password between {} and {} characters: ".format(PASSWORD_MINIMUM_LENGTH,PASSWORD_MAXIMUM_LENGTH))
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print("Password is too short.")
        while len(password) > PASSWORD_MAXIMUM_LENGTH:
            print("Password is too long.")
    print('*'*len(count))

def main():
    password=get_password(PASSWORD_MINIMUM_LENGTH,PASSWORD_MAXIMUM_LENGTH)
    print_asterisks(password)

def get_password(PASSWORD_MINIMUM_LENGTH,PASSWORD_MAXIMUM_LENGTH):
    password=input("Enter a password between {} and {} characters: ".format(PASSWORD_MINIMUM_LENGTH,PASSWORD_MAXIMUM_LENGTH))
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print("Password is too short.")
        while len(password) > PASSWORD_MAXIMUM_LENGTH:
            print("Password is too long.")
        password=input("Enter password between{} and {} characters: ".format(PASSWORD_MINIMUM_LENGTH,PASSWORD_MAXIMUM_LENGTH))
    return password

def print_asterisks(count):
    print('*'*len(count))

main()
