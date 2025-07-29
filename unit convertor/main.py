def length_converter():
    print("\n--- Length Conversion ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose option: ")
    value = float(input("Enter value: "))
    
    if choice == '1':
        result = value * 0.621371
        print(f"{value} km = {result:.2f} miles")
    elif choice == '2':
        result = value / 0.621371
        print(f"{value} miles = {result:.2f} km")
    else:
        print("Invalid choice!")

def temperature_converter():
    print("\n--- Temperature Conversion ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose option: ")
    value = float(input("Enter temperature: "))

    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value}°C = {result:.2f}°F")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(f"{value}°F = {result:.2f}°C")
    else:
        print("Invalid choice!")

def weight_converter():
    print("\n--- Weight Conversion ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose option: ")
    value = float(input("Enter weight: "))

    if choice == '1':
        result = value * 2.20462
        print(f"{value} kg = {result:.2f} lbs")
    elif choice == '2':
        result = value / 2.20462
        print(f"{value} lbs = {result:.2f} kg")
    else:
        print("Invalid choice!")

def main():
    while True:
        print("\n========= UNIT CONVERTER =========")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("4. Exit")
        choice = input("Select a conversion category: ")

        if choice == '1':
            length_converter()
        elif choice == '2':
            temperature_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
