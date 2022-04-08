"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    get_incomes(incomes)
    print_report(incomes)

def get_incomes(incomes):
    num_of_months = int(input("How many months? "))

    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)
    print_report(incomes)

def print_report(incomes):
    """Print incomes by month."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes)):
        income = incomes[month]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()