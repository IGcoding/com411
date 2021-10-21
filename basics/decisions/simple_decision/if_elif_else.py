# to identify from user input what way beep should paint
print("Towards which direction should I paint (up, down, left or right?")
direction = input()
print()
print()
if direction == 'up':
    print("I am painting in the upward direction")
elif direction == 'down':
    print("I am painting in the downward position")
elif direction == 'right':
    print("I am painting in the right position")
else:print("I am painting in the left position")
