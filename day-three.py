#check if the input string read the same as backward and forward

user_input = input("please enter the string to check if its palindrome : ")
rev_input = user_input[::-1]

if user_input == rev_input:
    print("the provided string is palindrome")
else:
    print("sorry look like we dont have a palindrome")