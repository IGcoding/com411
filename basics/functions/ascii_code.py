# this line of code will show program has started
print("Program has started!")
print("Please enter a standard character:")
character = input()
length = len(character)
print (length)
if length == 1:
    print (f"The ASCII code for {character} is {ord(character)}")

else:
    print ("Please enter only 1 character")
