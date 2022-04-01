"""1404/Thant_Zin_Oo
Pseudocode for temperature conversion
"""

MENU = ("C - Convert Celsius to Fahrenheit", "F - Convert Fahrenheit to Celsius","Q - Quit")

print(MENU)

choice = input("Choice:").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahremheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahremheit - 32)
        print(f"Result: {celsius:.2f} F")

    else:
        print("Invalid option")
    print(MENU)
    choice = input("Choices:").upper()
print("Thank you.")