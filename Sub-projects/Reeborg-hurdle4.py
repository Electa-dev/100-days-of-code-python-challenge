# My answer
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():  
    if wall_in_front() == True:
        turn_left()
    if wall_on_right() != True:
            turn_right()
            move()
    
while not at_goal():
    if wall_in_front() != True and wall_on_right() == True:
        move()
    elif wall_in_front() == True and right_is_clear() != True:
        jump()
    elif front_is_clear() == True and right_is_clear() == True:
        turn_right()
        move()


# Or Angela's
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():  
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front() == True:
        jump()
    else: move()


 




