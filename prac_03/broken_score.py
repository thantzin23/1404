def main():
    score = float(input("Enter your scores:"))

    while score < 0 or score > 100 :
        print ("Invalid scores!")
        score = float(input("Enter your scores:"))

    print("Your entered:",score)

    if score >= 50 :
        print("You pass!")
    elif score >=85 :
        print("Excellent!")
    else:
        print("Ah..oh")





main()