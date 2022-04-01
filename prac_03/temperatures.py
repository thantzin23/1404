Menu = ("C - convert celsius to fahrenheit , F - convert fahrenheit to celsius , Q - Quit")
print(Menu)
choice = input("Choice").upper()
while choice != "Q":
    if choice == "C":
            celsius = float(input("Enter temperature of celsius:"))
            fahrenheit = celsius * 9 / 5 + 32
            print (f"Result is :{fahrenheit:.2f}")

    elif choice == "F":
            fahrenheit = float(input("Enter temperature of Fahrenheit:"))
            celsius = fahrenheit *(5 + 32) / 9
            print (f"Result is :{celsius:.2f}")

    else:
            print("Invaild options!")
    print(Menu)
    choice = input("Choice").upper()

print("Thank You!")






