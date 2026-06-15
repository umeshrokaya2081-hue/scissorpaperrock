
print("=== Welcome to the Adventure Game ===")

name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"\nHello {name}! You are {age} years old.")

if age < 18:
    print("Sorry, you must be 18 or older to play.")
else:
    health = 10
    inventory = []

    print(f"\nYou start with {health} health.")

    wants_to_play = input("Do you want to play? (yes/no): ").lower()

    if wants_to_play != "yes":
        print("Maybe next time!")
    else:
        print("\nYour adventure begins!")

        direction = input("You reach a crossroads. Go left or right? ").lower()

        if direction == "right":
            print("You fall into a pit. Game Over!")
        elif direction == "left":

            lake = input(
                "You arrive at a lake. Swim across or go around? "
            ).lower()

            if lake == "across":
                health -= 5
                print(
                    f"A fish bites you! You lose 5 health. Health = {health}"
                )
            elif lake == "around":
                print("You safely walk around the lake.")
            else:
                print("Invalid choice. Game Over!")
                exit()

            key = input(
                "You find a key on the ground. Pick it up? (yes/no): "
            ).lower()

            if key == "yes":
                inventory.append("key")
                print("Key added to inventory!")

            monster = input(
                "A monster appears! Fight or run? "
            ).lower()

            if monster == "fight":
                health -= 3
                print(
                    f"You defeat the monster but lose 3 health. Health = {health}"
                )

                if health <= 0:
                    print("You have no health left. Game Over!")
                    exit()

            elif monster == "run":
                print("You escape safely.")
            else:
                print("The monster catches you. Game Over!")
                exit()

            place = input(
                "You see a house and a river. Where do you go? "
            ).lower()

            if place == "river":
                print("You fall into the river and lose.")
            elif place == "house":

                answer = input(
                    "The house is locked. Solve this puzzle: 7 + 5 = "
                )

                if answer != "12":
                    print("Wrong answer. Game Over!")
                else:
                    print("Correct! The door opens.")

                    if "key" in inventory:
                        print(
                            "You use the key to open a treasure chest!"
                        )
                        print(
                            "Congratulations! You found the treasure and won the game!"
                        )
                    else:
                        print(
                            "You entered the house, but without the key you cannot open the treasure chest."
                        )
                        print("You survive, but miss the treasure.")
            else:
                print("Invalid choice. Game Over!")
        else:
            print("Invalid choice. Game Over!")
