"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():# in main step put all def funtion befor def
    subject_details = get_data()
    print_subject (subject_details)
    #if there is any menu..
    #get user input
    #while user_input !="Q"
    #  if ..
    #     do_funtion(1)
    #  elif...
    #     do_funtion(2)
    # .....
    #  get user input

def print_subject(subject_details):
    for subject_detail in subject_details:
        print(f"{subject_detail[0]}is taught by {subject_detail[1]:12} and has {subject_detail[-1]:3} students")

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_detail =[]
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_detail.append(parts)

    input_file.close()
    return subject_detail # while return , delet all printing steps


main()
