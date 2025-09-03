def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for char in range(1, 7):
#    jump()

number_of_jumps = 6
while number_of_jumps > 0:
    jump()
    number_of_jumps -= 1
    if at_goal() == True:
        done()
    #print(number_of_jumps)

# Or we do this
while not at_goal():
    jump()
 




