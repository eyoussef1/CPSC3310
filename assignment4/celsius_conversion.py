ABSOLUTE_ZERO = -273.15

celsius_limit = int(input("Enter the Celsius degree to convert up to: "))

while celsius_limit < ABSOLUTE_ZERO:
    print("Error: Celsius cannot be below absolute zero.")
    celsius_limit = int(input("Enter the Celsius degree to convert up to: "))

print("Celsius Fahrenheit")

celsius = 0

while celsius <= celsius_limit:
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, fahrenheit)
    celsius += 1
