# Basic syntax..../////////..........///////////////................/////......./////..//

# // To map with real world scenarios , we started with OOPS in python ,
# class Student:
#     name = " ilyas khan"
#     roll_no = 23


# s1 = Student()

# print(s1.name)
# print(s1.roll_no)
# s2 = Student()
# print(s2.name)
# print(s2.roll_no)

# class Student:
#     def __init__(self,name,marks) :
#         print("Hello word!")
#         self.name = name
#         print(self)
#         self.marks = marks
#         print("adding student to the database...")
    

# s1 = Student("Waqas khan has gotted ", 98 )
# print(s1.name,s1.marks)

# s2 = Student("roman khan has gotted ", 90  )

# print(s2.name,s2.marks)
        


# class Student:
#     def __init__ (self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi",self.name, "Your avg score is :", sum/3)



# s1 = Student("Tony stalk",[98,89,79])
# s1.get_avg()

# class Student:
#     def __init__(self,name ,marks):
#         self.name = name 
#         self.marks = marks
    
#     def avg_marks(self):
#         sum = 0
#         for i in self.marks:
#             sum +=i
#         print("Hi " , self.name , "you have avg_score of about",sum/3)



# s1 = Student("Waqas khan",[98,75,97])
# s1.avg_marks()


# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account = acc
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs ",amount, "was debited :")
#         print("Total balance = ",self.get_balance())
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs ", amount ,"was credit")
#         print("Total balance = ",self.get_balance())
#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000,2000)
# acc1.debit(1000)
# acc1.credit(11000)


# class Student:
#     name = "karan khan"
#     roll_no = 45

# s1 = Student()
# print(s1.name)
# print(s1.roll_no)

# class Car:
#     color = "blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# class Student:
#     college_name= "ABDC"
#     def __init__(self,fullname,no,age):
#         self.name = fullname
#         self.no = no
#         self.age = age
#         print("adding some student to database...")
    
# s1 = Student("karan khan",45, 19)
# print("has fullname",s1.name,"rollNo of",s1.no,"and age of",s1.age,s1.college_name)


# s2 = Student("roman khan",34 ,18 )
# print("has fullname",s2.name,"rollNo of",s2.no,"and age of",s2.age,s2.college_name)

