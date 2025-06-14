# weight convertor in python 

# weight = float(input("enter you weight : "))
# unit  = input("kilograms or pounds ? (K or L)").upper()

# if unit == "K":
#     weight = weight *2.205
#     unit = "Lbs"
#     print(f"your weight is {round(weight,1)} {unit}")


# elif unit == "L":
#     weight = weight / 2.205
#     unit = "kgs"
#     print(f"your weight is {round(weight,1)} {unit}")
# else:
#     print(f"{unit} is invalid")


weight = float(input("What's your weight : "))
unit = input("Kilogram or pouds (K or L)").upper()
if unit == "L":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is {round(weight)} {unit}")
elif unit == "K":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"your weight is {round(weight)} {unit}")
else:
    print(f'{unit} is invalid ')
        