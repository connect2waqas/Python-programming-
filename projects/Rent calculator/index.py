rent = int(input("enter your total rent = "))
persons = int(input("enter the number of person = "))
electricity_bill= int(input("enter the electricity = "))
charge_per_unit = int(input("enter charge per unit = "))
food_order = int(input("enter food order = "))


total_bill = electricity_bill * charge_per_unit

total_rent = (total_bill + food_order + rent ) / persons

print(f"Monthly is aboout equal {total_rent}")
