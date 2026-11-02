
def main():
    date = input("Enter a date (mm/dd/yyyy): ").strip()

    parts = date.split("/")

    if len(parts) != 3:
        print("Error: Date must be in mm/dd/yyyy format.")
        return

    if not all(part.isdigit() for part in parts):
        print("Error: Date must contain numbers only.")
        return

    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
        return

    if day < 1 or day > 31:
        print("Error: Day must be between 1 and 31.")
        return

    print(f"{months[month - 1]} {day}, {year}")


if __name__ == "__main__":
    main()
