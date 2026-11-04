# Task 2: Temperature Converter

choice = input("Choose conversion (C or F): ")

if choice == "C":
    temperature = float(input("Enter temperature in Celsius: "))

    result = temperature * 1.8 + 32

    print(temperature, "°C =", result, "°F")

elif choice == "F":
    temperature = float(input("Enter temperature in Fahrenheit: "))

    result = (temperature - 32) / 1.8

    print(temperature, "°F =", result, "°C")

else:
    print("Invalid choice")
