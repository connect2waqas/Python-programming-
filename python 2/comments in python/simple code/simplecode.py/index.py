user1_house_size = float(input("Enter the size of house : "))
number_of_bedrooms1 = int(input("Enter the number of bedrooms :"))
user1_budgets = int(input("enter your budget : "))

user2_house_size = float(input("Enter the size of house : "))
number_of_bedrooms2 = int(input("Enter the number of bedrooms :"))
user2_budgets = int(input("enter your budget : "))

threshold_amount = 5700000
per_square_price = 5000

user1_house_price = user1_house_size * per_square_price
print(f"The price of house 1 {user1_house_price}")

user2_house_price = user2_house_size * per_square_price
print(f"The price of house 1 {user2_house_price}")

user1_threshold = user1_house_price >= threshold_amount
user2_threshold = user2_house_price >= threshold_amount

print("user 1 is paying above the threshold ", user1_threshold)
print("user 2 is paying above the threshold ", user2_threshold)
