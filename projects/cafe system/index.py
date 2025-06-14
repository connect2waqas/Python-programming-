print("<------Welcome to our Cafe------->")
print("Which food will you like to order here is the menu:-")
print("pizza :Rs 400")
print("pista :Rs 300")
print("badam : Rs 500")
print("coffee :Rs 80")

prices = {"pizza":400,
         "pista":300,
         "badam":500,
         "coffee":80,
         }

total = 0
while True:
    user_order = input("enter which of above would you like to order : (done / finish)").lower()

    if user_order =="done":
        print("Thank you of order ")
        break


    if user_order in prices:
        total += prices[user_order]
        print(f"your order {user_order} has been added ")
        print(f"Current Bill : Rs {total} ")
        
    
    else:
        print("sorry we don't have that's item ")
print(f"your total bill is {total} ")

print("<----Think You! Have a nice day---->")

    
