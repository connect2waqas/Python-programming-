# # List 
# numbers = [1,2,3,4,5]
# for number in numbers:
#     print(number*2)

# # Dictionary

# person = {"name": "Alice", "age": 25, "city": "New York"}

# for key , value in person.items():
#     print(f"{key}:{value}")


celsius_temperatures = [0, 10, 20, 30, 40]
farenhait_temp=[]

for temp in celsius_temperatures:
    farenhait= (temp*9/5)+32
    farenhait_temp.append(farenhait)
    print(farenhait_temp)