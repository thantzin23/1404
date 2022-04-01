"""1404/Thant_Zin_Oo"""

sales = float(input("Enter sales:$"))

while sales >=0:

    if sales < 1000 :
         result = sales * 10 / 100
         print ("The output:",result)
         sales = float(input("Enter sales:$"))


    elif sales >= 1000 :
        result= sales * 15 / 100
        print ("The output",result)
        sales = float(input("Enter sales:$"))

    else:
        print("Wrong output!")






