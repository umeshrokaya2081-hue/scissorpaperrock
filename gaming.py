print("Welcome to the Adventure game !")
name=input("What is your name ?")
age=int(input("What is your age?"))

print(f"|Hello {name} you are {age} years old. ")

health = 10 

if age >= 18:
    
    print(f"You are starting with {health} health.")
    wants_to_play = input("Do you want to play (Yes/No) ?")
    if wants_to_play == "Yes":
        print("Lets play !")
        

        left_or_right =input("First choice ... Left or right (Left/Right)? ").lower()
        if left_or_right=="left":
            ans= input("Nice , You follow the path and reach a lake... do you swim across or go around (across/around)?")

            if ans == "around":
                print("You went around and reached the other side of the lake.")

            elif ans=="across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health-=5

            else:
                print("You lose")

            ans=input("You notice a house and a river , which do you go to (river/house)?")
            
            if ans == "house":
                print("You go to the house and are greated by the owner .... He doesnot like you and you lose 5 health")
                health -=5
                if health<=0:
                    print("You now have 0 health and you loose the game ....")

            else:
                print("You fell in the river ans lost....")
    else:
        print("Cya.....")

else:
    print("Game over")

