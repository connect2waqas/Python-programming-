# so we have learn the map , filter and reduce function in python today

# def cube(x):
#     return x*x*x

# l = [1,4,5,6,7,9]

# newl = list(map(cube,l))

# print(newl)

# def square(x):
#     return x**2

# l = [2,5,6,7,8]

# newl = list(map(square,l))

# print(newl)

# l = [2,5,6,7,8]

# newl = list(map(lambda x: x**2,l))

# print(newl)

# l1 = [2,5,6,7,8]

# l2 = [3,5,3,7,3]

# l3 = [7,3,4,5,6]

# newl = list(map(lambda x , y, z: x + y + z,l1,l2,l3))

# print(newl)

# str_number = ["1","2","3","4","5"]

# int_number = list(map(int,str_number))

# print(int_number)

# names = ["bob","ilyas","abbas"]

# age = [23, 17, 12]

# combined = list(map(lambda name,age:f"{name} is {age} year old",names,age))

# print(combined)

# l = [2,3,5,6,7]

# newl = list(map(lambda x : x*x*x ,l))

# print(newl)

# printing even number through filter function

# numbers = [1,2,3,4,5,6,7,8]

# even_number = list(filter(lambda x : x % 2 ==0,numbers))

# print(even_number)


# numbers = [1,2,3,4,5,6,7,8]

# odd_number = list(filter(lambda x : x % 2 !=0,numbers))

# print(odd_number)

# examples in AI 

# data = ["data","","science","","machine learning","","deep learning"]

# filter_data = list(filter(lambda x:x !="",data))

# print(filter_data)

# data = ["data","","science","","machine learning","","deep learning"]

# filter_data = list(filter(lambda x : x != "",data))
# print(filter_data)

# # filtering

# l = [1,2,4,5,6,7,8,9,10,12]

# filterl= filter(lambda x : x < 11 ,l)

# print(list(filterl))

# l = [1,2,4,5,6,7,8,9,10,12]

# def filterted_l(x):
#     return x < 11

# filterted_data = filter(lambda x :filterted_l,l)

# print(list(filterted_data))

from functools import reduce

# number = [2,3,5,6,6,7]

# def reducnumber(x,y):
#     return x + y

# num_reduce = reduce(reducnumber,number)

# print(num_reduce)



# tuple1 = (2,3,4,5,6,7,8)

# reduce_tuple = reduce(lambda x , y: x + y,tuple1)

# print(reduce_tuple)

