# def display():
#     print("Hello world!")

# display()
# display()
# display()



# def net(x,y):
#     sum = x + y
#     product = x * y
#     return sum , product

# result = net(100,200)
# print(result)


# n = int(input("Please enter a number :"))

def check_number(n):
    i = 2
    is_prime = True
    while i < n:
     if n % 2 == 0 :
         is_prime = False
     i +=1
     return is_prime
    
check_number(12)
     
# if is_prime :
#     print("number is prime")

# else:
#     print("number is not prime")






