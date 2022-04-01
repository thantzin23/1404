"""CP1404- Practical
Thant Zin Oo
"""
#1
out_file = open("name.txt","w")
name = input("Enter your name :").upper()
print(name,file=out_file)

out_file.close()

#2
in_file = open("name.txt","r")
name = in_file.read()

in_file.close()

print("Your name is:",name)

#3
in_file = open("number.txt","r")

number_1 = in_file.readline()
number_2 = in_file.readline()

number_1 = int(number_1)
number_2 = int(number_2)
sum = number_1 + number_2

in_file.close()

print(number_1,"+",number_2,"=",sum)

#4

in_file = open("number.txt","r")

total = 0

for line in in_file:
    number_count = int(line)
    total += number_count

in_file.close()

print(total)

