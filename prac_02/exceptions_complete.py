"""CP1404- Practical
Thant Zin Oo
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        if result >= 0 :
                is_finished = True
        else:
            print("Invalid integer!Please enter a valid integer")
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)