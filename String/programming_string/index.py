# string are squence of character enclose in single or double qoutes

my_string = "Hello word!"

# there are two types of indexing in python
# 1) positive indexing
# 2) negitive indexing


str = "Hello"
print(str[1:2])
print(str[0:])
print(str[::-1])
print(str[:]) #print the hello without any changing

text = "python programming"

slice_text = text[0:6]
print((slice_text).upper())

slice_text = text[0::2]
print(slice_text.capitalize())

name = "waqas khan"

age  = 20

print("{} is {} year old.".format(name,age))

str = "Hello"

print("{} what is your name.".format(str))

text = "Python"
new_text = text[:2] + "x" + text[3:]  # "Pyxhon"

print(text[:2] + "x" + text[3:])

text = "Waqas khan"

print(text[0:4] + "r")

new_text = text.replace("khan","Ahmad")
print(new_text)


print(new_text)

a = "i am waqas"

print(a[0:10:2])

def extract_data_parts(date_string):
    year =int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:])

    return (year,month,day)

extract_data_parts("2024-04-05")

str = "Honesty is the best policy"
print((str[::-1]).capitalize())

def reversed_string(str):
    reversed_str= str[::-1]
    print(f"The reverse of {str} is '{reversed_str}'")

reversed_string(str=input("enter a string: "))

def reversed_string(str):
    reversed_str = str[2:9]
    print(reversed_str)

reversed_string(str=input("enter: "))

def helloword(str):
    reversed_str= str[1:6]
    print(reversed_str)

helloword(str=input("enter: "))

str = "Artificial"
print(str[:-4])
[:-4] removes the last 4 characters.
# Original String: "Artificial"
# Output after slicing: "Artifi"