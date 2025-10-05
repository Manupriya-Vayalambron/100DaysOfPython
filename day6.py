# ============================================
# Reeborg's Maze Solver
# --------------------------------------------
# Solves the maze challenge on:
# https://reeborg.ca/reeborg.html
#
# The robot uses the "right-hand rule" method 
# to navigate through the maze until it reaches 
# the goal. 
#
# Author: Manupriya Dhanush Vayalambron
# Language: Python (Reeborg Environment)
# ============================================

# Define a helper function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward until hitting a wall
while front_is_clear():
    move()

# Turn left to start following the wall
turn_left()

# Main loop — runs until the robot reaches the goal
while not at_goal():
    # If right side is clear, turn right and move
    if right_is_clear():
        turn_right()
        move()
    # If the path ahead is clear, move forward
    elif front_is_clear():
        move()
    # Otherwise, turn left to find a new direction
    else:
        turn_left()
