
# import random

# random_num = random.randint(1,100)

# # print(random_num)
# while True:
#     try:
#         guess = int(input('enter a number between 1 and 100 :'))
#         if guess < random_num:
#             print("Too low!")
#         elif guess > random_num:
#             print("Too high!")
            
#         else:
#             print("Congrulation you guessed the number!")
#             break
#     except ValueError:
#         print("please enter a valid number")

# import random 

# random_num = random.randint(1,100)
# try:
#  while True:

#     guess = int(input("guess the number "))
#     if guess < random_num:
#         print("Too low")
#     if guess > random_num:
#         print("Too high")
#     else:
#         print("congrulation you guessed the number",guess)
# except ValueError:
#     print("please enter a valid number")


#  random guessing game 

import random 


random_num = random.randint(1,100)

while True:
  try:

 

    guess = int(input("guess a number between the 1 and 100 :"))

    # random_num = random.randint(1,100)

    if guess < random_num:
        print("Too low")
    elif guess > random_num:
        print("Too high")
        
    else:
        print("Congrulation you win the game")
        break

  except ValueError:

    print("please enter a valid number")