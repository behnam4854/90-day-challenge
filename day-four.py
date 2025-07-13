# write a programm that calculate the factorial of desiered number

def fact(n):
    """ calculates the factorial of n"""
    return 1 if n == 1 else n * fact(n - 1)


number = input("Enter the number to calculate the factorial of: ")
print('The factorial of the number is : ', fact(int(number)))