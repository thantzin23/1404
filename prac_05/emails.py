def main():

    email_to_name ={}
    email = input("Email:")

    while email !="":
        name = name_for_email(email)
        comfrim = input(f"Is that your name {name} (Y?N) ?").upper()

        if comfrim != "Y" and email !="":
            print("Name:")
        email_to_name[email] = name
        email = input("Email:")

    for email,name in email_to_name :
        print(f"{email} ({name})")

def name_for_email(email):
    profile = email.split('@')[0]
    part = profile.split
    name = "".join(part).title()
    return name






main()