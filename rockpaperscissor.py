# <!-- """
# workflow of project 

# 1- input from user (rock,paper, scissor)
# 2- computer choice(computer will choose randomly not conditionally)
# 3. Result print


# cases 
# A- rock 
# rock -rock = tie
# rock paper = paper win
# rock -scissior = rock win 

# B- paper 
# Papaer - Paper  = tie
# paper -rock = paper win 
# paper - scissor = scissor win

# C- Scissor
# scissio-scissor = tie
# scissor -rock = rock win
# scissor - paper= scissor win


# """"
import random
item_list = ["rock", "paper", "scissor"]

# 1. Start an infinite loop
while True:
    user_choice = input("\nEnter your choice (rock, paper, scissor) or type 'quit' to exit: ").lower()

    # 2. Give the user a way to break out of the loop
    if user_choice == 'quit':
        print("Thanks for playing! Goodbye.")
        break  # This stops the loop completely
        
    # 3. Check for invalid input early
    if user_choice not in item_list:
        print("Invalid input! Please choose rock, paper, or scissor.")
        continue  # This skips the rest of the code and jumps back to the input prompt

    comp_choice = random.choice(item_list)
    print(f"Computer choice = {comp_choice}, User choice = {user_choice}")

    # --- Your Game Logic ---
    if user_choice == comp_choice:
        print("It's a tie!") 
    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper wins! Computer wins!")
        else:
            print("Rock wins! User wins!")     
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("Paper wins! User wins!")
        else:
            print("Scissor wins! Computer wins!")
    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("Rock wins! Computer wins!")
        else:
            print("Scissor wins! User wins!")