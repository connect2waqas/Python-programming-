# here is the part 2 of list in python in which we will have to disscus about the builtin function for python.
# these builtin function can be use to manipulate the list like :
# 1) modifying the list
# 2) extending the list
# 3) concatenation of the list
# 4) appending to the list
# 5) Removing the element
# 6) poping the list
# 7) counting element in the list
# 8) reversing the list
# 9) Adding to list

# properties of list:
# 1) mutable
# 2) stored mix data type
# 3) zero-indexing 
# 4) ordered 


mix_list = [1,2,3,"Hello", True]

print(mix_list[3] == 4) #it return a boolean value true or false

mix_list[3] = 4
print(mix_list)

number_to_text = [12,13,14,15,16,17,18,19,20,21]

number_to_text[2:4] = ["books","pen","bag"]

print(number_to_text)
a = [1,2,3,4,5]

a[2:4] = ["books"] # it will take the space of two element in the element the book will take the place of one element and list index will be 
# decrease by one

print(a)

thislist = []

thislist.append("book")

print(thislist)

# Removing element from the list

a = [1,2,3,4,5,6,7,8,9,10] 
# 1) pop() method
# it removes and returns the last element from the list
b = (a.pop())
print(b)

# 2) remove()  remove the first occurance of the element 

b = a.remove(1)
print(b, a) #it only remove index element from the list but not returns the value by printing

# 3) clear() method : it remove all the element from the list and donot return the list

a = [1,2,3,4,5,6,7,8,9,10] 
b = (a.clear())
print(b)

a = [" "," "," "," "]
print(len(a))

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = ["hello","word"]
concatenation = a + b

print(len(concatenation))

print(a + b + c)

# 4) in keyword in python

b =  2 in a or 7 in a
print(type(b))

print(b)

a =[]
b = 2 in a
print(b)

a = [1,2,3,4,5]

a.reverse()
print(a)

a = [1,2,3,4,5]
b = a.copy()
print(b)

a = [1,2,3,4,5]

a.reverse()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
print((a.reverse()))

a = [1,2,3,4,5]
a.reverse()
print(a)

print(a.reverse())

a = [1,2,3,4,5]
b = [6,7,8,9,10]

a.extend([b])

print(a)

