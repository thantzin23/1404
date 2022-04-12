"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

line_num = 6
min_num = 1
max_num = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    user_input = int(input("How many quick picks? "))
    while user_input < 0:
        print("Enter again !")
        user_input = int(input("How many quick picks? "))

    for i in range(user_input):
        quick_pick = []
        for j in range(line_num):
            number = random.randint(min_num, max_num)
            while number in quick_pick:
                number = random.randint(min_num, max_num)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))



main()


