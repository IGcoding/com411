#program to compare 2 numbers and return a comparision
print("please enter the first number.")
input1 = input()
print(input1)
print("Please enter the second number")
input2 = input()
print(input2)
if input1 < input2:
    print("The first number is the smallest")
elif input1 > input2:
    print ("The second number is the smallest")
elif input1 == input2:
    print("Both are equal")
