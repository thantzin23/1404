"""CP1404- Practical
Thant Zin Oo
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# when we put charater or non-integer , the value error will occur
# when we put 0 to denominator , the zero division error
# No , if we put non-zero integer , we can say yes
