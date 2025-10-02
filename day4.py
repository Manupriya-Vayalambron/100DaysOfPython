import random

# ASCII art for Rock
# Source: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# ASCII art for Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices for easier access
choices = [rock, paper, scissors]

# Main game loop
while 1:
    # Ask the player for input
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    
    # Check if input is valid
    if 0 <= player and player <= 2:
        # Display player's choice
        print(choices[player])
        print("Computer chose: ")
        
        # Randomly generate computer's choice
        computer = random.randint(0, 2)
        print(choices[computer])
        
        # Determine the winner
        if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
            print("You Won")
        elif (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
            print("You Lose")
        else:
            print("Its a draw")
    else:
        # Handle invalid input
        print("Invalid input")
    
    # Ask if the player wants to play again
    move = int(input("Type 1 to start new game and 0 to stop game: "))
    if move == 0:
        exit(0)
