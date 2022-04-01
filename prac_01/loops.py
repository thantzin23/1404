"""1404/Thant_Zin_Oo"""

for i in range (1,21,2):
    print(i,end=' ')

print()

for j in range (0,101,10):
    print(j,end=' ')

print()

for k in range (20,0,-1):
    print(k,end=' ')

print()


def main ():
    stars = int(input("Numbers of stars:"))

    for i in range(stars):
        print('*'* stars)

    for i in range (stars):
        for j in range(i+1):
            print("*",end='')
        print()


main()

