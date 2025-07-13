# get an inter value and return sum of its digits, as simple as that

number = input("Please enter a Inter Value : ")
sum = 0
list_comprehetion = [int(x) for x in number]
for i in range(len(list_comprehetion)):
    sum += list_comprehetion[i]
print(list_comprehetion)
print("sum of the digits is : ", sum)
