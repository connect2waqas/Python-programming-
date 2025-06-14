class Bank:
    def __init__(self):
        self.balance = 0
    def show_balance(self):
        print(f' your balance is {self.balance:.2f}')
    def deposit(self):
        amount = int(input("enter amount : "))
        if amount <=0:
            print(f"That's invalid {amount}")
            return 0
        else:
            self.balance +=amount
            print(f" Your deposit amount is {amount}")
        
    def withdraw(self):
        global balance
        amount = int(input("enter amount"))
        if amount > self.balance:
            print("insuffienct balance")
        else:
            self.balance -= amount
            return amount
            

bank_account = Bank()


is_running = True

while is_running:
        print("\n<---- Bank Menu ---->")
        print("1.check balance")
        print("2.deposit money")
        print("3.withdraw")
        print("4.exit")
        user_choice = int(input("enter : "))
        if user_choice == 1:
            bank_account.show_balance()
        elif user_choice == 2:
            bank_account.deposit()
        elif user_choice == 3:
           bank_account.withdraw()
        elif user_choice ==4:
            is_running == False
        else:
            print("That's invalid choice ")
print("Thanks You ! Have a nice day ")