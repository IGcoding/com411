# this line of code will show program has started
print("Program has started!")
print("Please enter a standard character:")
# this line will store user input so len function can be used to determine number of characters
character = input()
length = len(character)
print (length)
# following if statement then works out ASCII value of user input character and returns to user
if length == 1:
    print (f"The ASCII code for {character} is {ord(character)}")

else:
    print ("Please enter only 1 character")
print("Program ended!")
