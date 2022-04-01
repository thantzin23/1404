"""1404/Thant_Zin_Oo"""

num_of_items = int(input("Number of items:"))

total_amount = 0

while num_of_items < 0:

    print("invalid number.txt!")

for i in range(num_of_items):

    price_of_items = float(input("Price of items:"))

    total_amount += price_of_items

if total_amount > 100:

    total_amount = total_amount * 90 / 100

print(f"Total price for {num_of_items} items is ${total_amount:.2f}.")
