# String Part-2
str = "Hello my name is waqas"
print(len((str).strip()))
print(len(str))

# string with special word
s = "Hello\nword" # but it is consider one word okay
print(s)
print(len(s)) # special symbol can also be count in lengthing of string okay . point to be noted
statement = """Data science is a multidisciplinary field that combines mathematics, statistics, computer " 
          science, and domain expertise to extract meaningful insights from data, enabling informed
          decision-making and strategic planning"""
print("The length of the above statement before removing whitespaces is", len(statement))

new_length = statement.replace(" ","")
print("The length of the above statement after removing  whitespaces is",len(new_length))

str ="Helloword"
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.upper())

# string concatenation

str1 = "Hello "
str2 = "world"

full_str = str1 + str2

print(full_str)

print(str1 + str2)

print("".join([str1 , str2]))

# string replacing 

str1 = "Helloword"
print(str1.replace("word","waqas"))

text = "Hello i am learning python"

def replace(text):
    print(text.replace("python","java"))

replace(text)

text = """I hate the way hate festers in silence, how it twists even
the kindest hearts into knots of resentment. I hate how hate spreads
like wildfire, fueled by misunderstandings and fear, leaving ashes of 
trust in its wake. I hate that hate lingers in whispered rumors, in  
bitter glances, in the cold shoulders that fracture friendships. But 
what I hate most is how easily hate disguises itself as righteousness,
how it justifies cruelty with hollow logic, and how it convinces us 
that division is strength. To hate is easy; to rise above it takes courage" 
I am still learning to muster."""

def replace(text):
    new_text = text.replace("hate","love")
    # print(new_text.replace(" ",""))
    print(new_text)
    print(text)
replace(text)

print(text.index("hate"))
text1 = "Hello"
text2 = "world"
# here we have to solve a question base on string and by function
def string_fun(text1,text2):
    full_text = "".join([text1,text2])
    print(full_text)
    print(len(full_text))
    extracted_text = full_text[5:]
    print(extracted_text)
    reversed_text = extracted_text[::-1]
    print(reversed_text)
    text_upper = reversed_text.upper()
    print(text_upper)
    replace_chr = (text_upper.replace("L","X").upper())
    print(replace_chr)
string_fun(text1=input("enter: "),text2=input("enter: "))

a = 5
b = a
print(id(a) == id(b))
print(id(a))
print(id(b))

text = "python programming"
text1 = text
print(id(text))
print(id(text1))
print(id(2651945909680))
# split method 
# it can be used to splite the string into a list

text = "Programming"
list_text = []
print(text.split(","))
for i in text:
    list_text.append(i)
print(list_text)
print(len(list_text))

# Startwith() function

text = "Python Programming"

while text:
    if text.startswith("Py"):
        print("Found")
        break
    else:
        print("Not found")
        break

# Endwith() function 
count = True
while count:
    if text.endswith("p"):
        print("correct")
        count = False
    else:
        print("incorrect")
        break
text = "python programming"
print(text.find("p","y"))


text = """I hate the way hate festers in silence, how it twists even
the kindest hearts into knots of resentment. I hate how hate spreads
like wildfire, fueled by misunderstandings and fear, leaving ashes of 
trust in its wake. I hate that hate lingers in whispered rumors, in  
bitter glances, in the cold shoulders that fracture friendships. But 
what I hate most is how easily hate disguises itself as righteousness,
how it justifies cruelty with hollow logic, and how it convinces us 
that division is strength. To hate is easy; to rise above it takes courage" 
# I am still learning to muster."""

def replace_space(text):
    print(text.replace(" ","-"))
replace_space(text)

        