# class User:

#     def login(self):
#         print("login")
    
#     def register(self):
#         print("Register")
    

# class Student(User):

#     def enroll(self):
#         print("enroll")
#     def review(self):
#         print("review")

# u = Student()
# u.login()
# u.enroll()
# u.review()
# u.register()

# let we have print a pyramid through the basic methods

# print("     *  ")
# print("    * *  ")
# print("   * * *  ")
# print("  * * * * ")
# print("   * * *  ")
# print("    * *  ")
# print("     *  ")

# lets we have to create it through another method

row = int(input("enter the number of rows ="))
k = 0
for i in range(1, row +1):
    for space in range(1,(row-i)+1):
        print(end=" ")
    k = 0
    while k!=(2 * i - 1):
        print("*",end="")
        k +=1
       
    print()
# row = int(input("Enter the number of rows = ")) 
# for i in range(1, row + 1):
#     # Print spaces for the pyramid alignment
#     for space in range(1, (row - i) + 1):
#         print(end=" ")

#     # Initialize k for each row and print stars
#     k = 0
#     while k != (2 * i - 1):
#         print("*", end="")
#         k += 1

#     # Move to the next line after each row
#     print()
