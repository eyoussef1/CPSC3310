ABSOLUTE_ZERO = -459.67
temperature = float(input("Enter the temperature: "))
conversion = input(
    "Enter F to convert Fahrenheit to Celsius, or C to convert Celsius to Fahrenheit: ")
if conversion == "F":
    if temperature >= ABSOLUTE_ZERO:
        celsius = (temperature - 32) * 5 / 9
        print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius")
    else:
        print("Invalid temperature. Temperature cannot be below absolute zero.")
elif conversion == "C":
    if temperature >= -273.15:
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"{temperature} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit")
    else:
        print("Invalid temperature. Temperature cannot be below absolute zero.")
else:
    print("Invalid conversion choice.")
