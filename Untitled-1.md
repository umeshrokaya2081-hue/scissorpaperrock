<!-- """
workflow of project 

1- input from user (rock,paper, scissor)
2- computer choice(computer will choose randomly not conditionally)
3. Result print


cases 
A- rock 
rock -rock = tie
rock paper = paper win
rock -scissior = rock win 

B- paper 
Papaer - Paper  = tie
paper -rock = paper win 
paper - scissor = scissor win

C- Scissor
scissio-scissor = tie
scissor -rock = rock win
scissor - paper= scissor win


"""" -->
import random
item_list = ["rock", "paper", "scissor"]

user_choice= input("Enter your choice (rock, paper, scissor): ").lower()

comp_choice = random.choice(item_list)

print(f"Computer choice=,{comp_choice}, user Choice = { user_choice}")

if user_choice == comp_choice:
  