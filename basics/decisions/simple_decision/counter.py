#program to compare 3 numbers and identifiy and count how many are odd or even
print("Please enter the first number")
number1 = int(input())
print(number1)
print("please enter second number")
number2 = int(input())
print(number2)
print("Please enter third number")
number3 =int(input())
print(number3)
even = 0
odd = 0
if number1 % 2 == 0:
    even += 1
else:
    odd += 1
if number2 % 2 == 0:
    even += 1
else:
    odd += 1
if number3 % 2 == 0:
    even += 1
else:
    odd += 1
print()
print()
print (f"there were {even} even and {odd} odd numbers")

