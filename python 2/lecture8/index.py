# print("Hope to skill")

# assing to variables 

# a = "Hope to skill"
# print(a)

# multiline  String

# ai = """something can be written on it in the multiline and can be used in the nlp and post processing unit"""


#  Modifyin the string 

#  Upper case 

# a = "hello, word!"

# print(a.upper())

# print(ai.upper())


# lower case

# print(a.lower())

# Removing the Whitespaces

# whitespace = """    something can be written on it in the multiline
                # and can be used in the nlp and post processing unit    """

#  By the use of method 

#  it can only handle the whitespaces of the start and end!

# print(whitespace.strip())

# Replace the string


# str= " Hello, word!"

# print(str.replace("Hello","Hi"))

# Split the string

# str = "Hello, word!"

# print(str.split(","))


# slicing in python 

# word = "Python"

# print(word[0])
# print(word[-1])

# word = "Artificial intelligence"

# print(word[0:11])

# print(word[11 :])

# print(word[-1])

# 2. Common Operations on Strings:

# concatenation:

# word1 = "artificial "

# word2 = "intelligence"

# word3 = word1 + word2

# print(word3)

# Repitation : using item more time you want 


# word = "Artificial intelligence "

# print(word * 3)

# Membership : checking weather that part exist in the string like:

# print("intelligence " in word )

# print(word.upper())

# print(word.title())

# print(word.lower())

# Removing the spaces 

# word = "  AI is awesome"

# print(word.strip())

# word = "Artificial intelligence "

# print(word.replace("intelligence","learning"))

# Note : list items into string 

# word = ["AI", " is ", "awesome"]

# print("".join(word))

# list = ["I", " love ", " You"]

# print(" ".join(list))


# String formating 

# name = "waqas"

# age = 19

# print(f"My name is {name} and i am about {age} year old...")

# # using format() method

# print("My name is {} and i am {} year old".format(name,age))

# print("My name is %s and i am %d year old."%(name,age))

# word = "Python "

# print(word.swapcase())

# reversed_word = word[::-1]

# print(reversed_word)

# str = "options"

# reversed_options = str [::-1]

# print(reversed_options)

# word = "Hello word "

# print(word.center(25, "*"))

# print(word.ljust(20, "-"))

# word = "Artificial intelligence"

# print(word.count("a"))

# print(word.count("A"))

# print(word.find("intelligence"))

# print(word.count("intelligence"))

# print(word.count("Arti"))

# print(word.count("l"))

# print(word.index("intelligence"))

# Checking String Characteristics:

# word = "waqas"

# print(word.isdigit())

# print(word.isalpha())

# num= 3229809895

# print(num.is_integer())

# print("12345".isdigit())

# 6. Escaping Characters:

# word = "He said,\"Hello word!\""

# print(word)

# a = "He said that i am learning \"artificial intelligence\""

# print(a)

# String encoding and decoding : mean that how to convert the string into binary or machine readable language.

s = "Hello word!"

s_encode = s.encode("utf-8")

print(s_encode)

s_decoded =s_encode.decode("utf-8")

print(s_decoded)
