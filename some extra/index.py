# age = 16
# has_license = False

# if age >= 18:
#     if has_license:
#         print("You can drive.")
#     else:
#         print("You need a license to drive.")
# else:
#     print("You are too young to drive.")



# class Car():
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model = model
    
#     def fullname(self):
#         return f"{self.brand} {self.model}"



# my_car = Car("Honda","Civic")
# print(f"your car {my_car.model},is very fansive")
# print(f"your car {my_car.brand},is very high rated")
# print(my_car.fullname(),"is your best car model and brand : ")

# class Area():
#     def __init__(self,length,width):
#         self.len = length
#         self.wid = width

#     def Total_area(self):
#         self.area = self.len * self.wid
#         return self.area
        


# area1 = Area(20,30)
# print(area1.len)
# print(area1.wid)
# print("Total area :",area1.Total_area())



class Car():
    def __init__(self,brand,model):
        self.brand= brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla= ElectricCar("Tesla","Model S", "85Kwh")
print(my_tesla.model)






my_car = Car("Honda","Civic")