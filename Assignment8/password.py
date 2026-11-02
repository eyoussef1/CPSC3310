
def main():
    password = input("Enter a password: ")

    valid = True

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        valid = False

    if not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
        valid = False

    if not any(char.islower() for char in password):
        print("Password must contain a lowercase letter.")
        valid = False

    if not any(char.isdigit() for char in password):
        print("Password must contain a number.")
        valid = False

    if not password.isalnum():
        print("Password must contain letters and numbers only.")
        valid = False

    if valid:
        print("Password is valid.")
    else:
        print("Password is invalid.")


if __name__ == "__main__":
    main()
