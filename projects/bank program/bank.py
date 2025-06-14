# # #  so i have to do it for two time so the more we practace the more we will understand it . so we should
# # #  do it for two time more 
# # #  let begin

# def show_balance():
#     print(f"Your balance is {balance:.2f}")

# def deposit():
#     amount = float(input("enter the amount to deposited : "))
#     if amount < 0:
#         print("That's invalid amount")
#         return 0    
#     print(f"You deposited {amount}")
#     return amount

# def withdraw_money():
#     global balance
#     amount = float(input("enter the amount to be withdraw : "))
#     if amount < 0:
#         print("That's is invalid amount")
#     elif amount > balance:
#         print("Insufficient balance")
#     else:
#         balance-= amount
#     print(f"You have withdraw {amount} ")

# balance = 0

# is_running = True

# while is_running:

#     print("1. Show balance")
#     print("2. deposit money")
#     print("3. withdraw money")
#     print("4.Exit Account")

#     choice = int(input("enter a number (1-4) : "))
#     if choice == 1:
#         show_balance()
#     elif choice == 2:
#         balance += deposit()
#     elif choice == 3:
#         withdraw_money()

#     elif choice == 4:
#         is_running = False
#     else:
#         print("That's is invalid choice")

# print("Thank You! Have a nice day")

# # def show_balance():
#     print(f"Your balance is {balance:.2f}")

# def deposit():
#     amount = float(input("Enter the amount you want to deposited :"))
#     if amount < 0:
#         print(f"That's invalid amount {amount}")
#         return 0
#     else:
#         print(f"Your  deposited amount is {amount}")
#         return amount
    


# def withdraw():
#     global balance
#     amount = float(input("Enter the amount you want to withdrawn :"))
#     if amount < 0:
#         print("That's invalid amount")
#     elif amount >  balance:
#         print("Insufficient balance")
#     else:
#         balance -= amount
#         print(f'Your withdraw amount is {amount}')


# balance = 0
# is_running = True

# while is_running:
#     print("1.Show balance")
#     print("2.Deposit")
#     print("3.Withdraw")
#     print("4.Exit")

#     choice = int(input("Enter a number between (1-4) :"))

#     if choice == 1:
#         show_balance()

#     elif choice == 2:
#          balance += deposit()
#     elif choice == 3:
#          withdraw()
#     elif choice == 4:
#          is_running = False
#     else:
#          print("That's invalid choice")
# print("Thank You! Have a nice day")



# class Fraction:
#     def __init__(self, numerator , denomeroter):
#         self.numerator = numerator
#         self.denomeroter = denomeroter

#     def __str__(self):
#         return "{}/{}".format(self.numerator,self.denomeroter)
    
#     def __add__(self,other):
#         temp_num = self.numerator * other.denomeroter + other.numerator *self.denomeroter
#         temp_den = self.denomeroter * other.denomeroter
#         return "{}/{}".format(temp_num,temp_den)
    
#     def __sub__(self,other):
#         temp_num = self.numerator * other.denomeroter - other.numerator *self.denomeroter
#         temp_den = self.denomeroter * other.denomeroter
#         return "{}/{}".format(temp_num,temp_den)
    
    
#     def __multiplication__(self,other):
#         temp_num = self.numerator *  other.numerator
#         temp_den = self.denomeroter * other.denomeroter
#         return "{}/{}".format(temp_num,temp_den)
        


# x = Fraction(9 , 5)
# y = Fraction(3,6)

# print(x)
# print(y)

# print ( x * y)

# print(x+y)

# def show_balance():
#     print(f"your balance is {balance:.2f}")




# balance = 0

# is_running = 0

# while is_running:
#     print("enter 1 to show the balance ")
#     print("enter 2 to deposit money..")
#     print("enter 3 to withdraw money..")
#     print("enter 4 to to Exit")

# choice = int(input("enter you choice (1-4) ..."))
# if choice == 1:
#     show_balance()
# num1 =int(input("enter a number  "))

# operator = input("enter an operator + - / * ")

# num2 = int(input("enter a second number "))

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)