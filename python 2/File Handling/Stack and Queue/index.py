
# stack = []

# while True:
#     q = input('enter 1 to push \n enter 2 to pop \n enter 0 to break :')
#     if q =='0':
#         break
#     elif q == "1":
#         name = input("enter a name :")
#         stack.append(name)
#     elif q == "2":
#         if len(stack)<=0:
#             print("Stack is empty , you cannot pop any item")
#         else:
#                x = stack.pop()
#                print(f"The pop is item is {x}")
        
#     else:
#          print("invalid input")
#     print(stack)     


# # print(stack)


# name_collection = []

# while True:
#     name = input(" Enter your name here")
#     name_collection.append(name)


name= []
max_enteries= 5
while True:
    a = int(input("enter a number a:"))
    b = int(input("enter  number b :"))
    addition = int(input((f"enter the sum of {a} and {b}")))
    if addition == a + b :
        name.append(addition)
        print("you enter answer is right")
        if len(name) ==5:
            break
    else:
        print("your enter wrong try again :")
    
    print(name)


# name = []
# max_entries = 5  # Limit to 5 correct entries

# while True:
#     try:
#         a = int(input("Enter number a: "))
#         b = int(input("Enter number b: "))
#         addition = int(input(f"Enter the sum of {a} and {b}: "))
        
#         if addition == a + b:
#             name.append(addition)
#             print("Correct! The sum has been added to the list.")
#             if len(name) >= max_entries:
#                 print("You've reached the maximum number of entries.")
#                 break
#         else:
#             print("You entered the wrong sum. Try again.")
        
#         print("Current list of correct sums:", name)
    
#     except ValueError:
#         print("Please enter valid numbers only.")

    


    