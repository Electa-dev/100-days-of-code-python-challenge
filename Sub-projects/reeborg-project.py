# Make the robot jump hurdles
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_three():
    move()
    move()
    move()
def turn_around():
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
    
for char in range(1, 7):
    jump()
        
 




