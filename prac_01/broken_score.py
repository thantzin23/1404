"""1404/Thant_Zin_Oo"""



def main():
        score = float(input("Enter score: "))

        while score < 0 and score > 100 :
                print ("invalid score!")
                score = float(input("Enter score: "))

        print ("you entered ",score)
        if score >=50 :
                print("passable")
        elif score >=90 :
                print ("excellent!")

        else:
                print("bad!")

main()

