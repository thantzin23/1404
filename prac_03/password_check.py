password = "Zin223"

get_password = input("Enter your password:")


while get_password !=password :
    print("Invalid password!")
    get_password = input("Enter your password:")
if get_password == password:
    print ("Correct this your password")
else:
    print("Enter again!")