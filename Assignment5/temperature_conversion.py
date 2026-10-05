
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


def get_temperature_type():
    while (temperature_type := input(
            "Enter the type of temperature (F for Fahrenheit, C for Celsius): "
    ).upper()) not in ("F", "C"):
        print("Invalid temperature type.")

    return temperature_type


def get_temperature(temperature_type):
    while True:
        try:
            temperature = float(input("Enter the temperature: "))

            if temperature_type == "C" and temperature < ABSOLUTE_ZERO_C:
                print("Temperature cannot be below absolute zero.")
            elif temperature_type == "F" and temperature < ABSOLUTE_ZERO_F:
                print("Temperature cannot be below absolute zero.")
            else:
                return temperature

        except ValueError:
            print("Invalid temperature. Please enter a number.")


def display_conversion(temperature_type, temperature):
    if temperature_type == "F":
        celsius = (temperature - 32) * 5 / 9
        print(f"{temperature:.2f} Fahrenheit = {celsius:.2f} Celsius")
    else:
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"{temperature:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")


if __name__ == "__main__":
    main()
