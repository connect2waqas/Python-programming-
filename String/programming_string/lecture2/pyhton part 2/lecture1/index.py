# list is a data structure that store multiple values in one variable
# list has my contain different other data structure as values
# list are that data structure data can multiple at a time 
# list are mutable mean we can add, remove and modify it
# list values may be other list, tuple, a string , any numberical values

empty_list = []

mix_list = ["Waqas",True,4.13,[1,2,3,'roman']]

numeric_list = [100,200,300,400,500]

print(empty_list)
print(mix_list)
print(numeric_list)

print(numeric_list.extend(mix_list))

mix_list =["Waqas","123",str(True),str(False),[1,2,3]]

# print(mix_list[::-1])

for i in mix_list:
    print(i[::-1])

# This is called the jogary programmar😂😊😂🤣❤🌹

mix_list = ["waqas","😂😊😂🤣❤🌹"]

for i in mix_list:
    print(i[::-1])

Slicing in list:

mix_list = [20,30,"waqas",True,[1,2,3]]

new_list = (mix_list[0:3])

print(new_list)

print(mix_list[0::2])

numeric = [1,2,3,4,5,6,7,8,9,10]

for i in numeric:
    if i % 2==0:
        print(i,end=" ")

print(numeric[-5:])

print(numeric[-2::2])


print(numeric[::3])  #this we have a gap of 2 and so on

score = [55,89,76,63,93,50,72]

empty_list = []

for i in score:
    if i > 70:
        empty_list.append(i)
    else:
        pass
       

print(empty_list)

data = [1,2,3,4,5,6,7,8,9,10]

sum_first_five = sum(data[:5])
print(f"The sum of the first element is {sum_first_five}")
reversed_list = data[::-1]
print(f"The reversed list is {reversed_list}")

list_number = [1,2,3,4,5,6,7,8,9,10]

def swapping(list_number):
    new_list1 = list_number[0:5] # here the index no 5 can be ignore okay
    new_list2 = list_number[5:] # here the slicing start from the index 5 and so on
    print(new_list1,"\n",new_list2)
    swapped_list = new_list2 + new_list1
    print(f"The swapping of list is {swapped_list}")
    sum_list = sum(list_number[7:])
    print(sum_list)
swapping(list_number)

# what is the output of the following code

numbers = [1,2,3,4,5]
new_number = numbers[2:4]
print(new_number)