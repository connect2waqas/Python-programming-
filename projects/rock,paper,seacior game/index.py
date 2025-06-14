# import random

# emojis = {"r":"🛤","s":"✂","p":"📄"}
# choices = ("r","p","s")

# while True:

#     user_choice = input("Rock,Paper,scissors(r/p/s)").lower()
#     if user_choice not in choices:
#         print("invalid choice")
#         continue
        
#     computer_choice = random.choice(choices)

#     print(f"You chose {emojis[user_choice]}")
#     print(f"computer chose {emojis[computer_choice]}")

#     if user_choice == computer_choice:
#         print("Tie!")
#     elif user_choice == "r" and computer_choice == "s":
#         print("You win")
#     elif user_choice == "s" and computer_choice == "p":
#         print("You win")
#     elif user_choice == "p" and computer_choice == "r":
#         print("You win")
        
#     else:
#         print("You lose!")
    
#     should_continue = input("Continue?(y/n)").lower()

#     if should_continue == "n":

#         break


import random

choices = ("r","s","p")

emojis = {"r":"🛤","s":"✂","p":"📃"}

while True:

    user_choice = input("Rock , Paper , scissor (r/s/pa)")
    if user_choice != "y" and user_choice == "n":
        print("Invalid choice!")
        continue
        

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"computer choice {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("You Tie!")
    elif user_choice =="r" and computer_choice =="p":
        print("You win")
    elif user_choice =="s" and computer_choice == "r":
        print("You win")
    elif user_choice =="p" and computer_choice == "s":
        print("You win")
    else:
        print("You lose ")

    should_continue = input("Continue ? (y/n)").lower()

    if should_continue == "n":
        break




