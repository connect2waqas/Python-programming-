# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# in it we can read in file its character and also all of its entire filef = open("demo.txt", "r")
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# ///////........./////.......//////............../////////.......////////......////.......////.......///

# f = open("demo.txt", "r")
# line1 = f.readline()
# print(line1)
# print(type(line1))
# f.close()
# Here we the extre space if we have to remove it we can use the strip() Method
# ////////............//////////////////...........///////............///////////////............///////.////

#  HERE IS THE SOLUTION

# f = open("demo.txt", "r")
# line1 = f.readline()
# print(line1.strip())
# print(type(line1.strip()))
# f.close()

# /////...............////////////...................///////////...............////////////....../////....///


# f = open("demo.txt", "w")

# data = f.write("\n and also machine learning ")
# print(type(data))
# f.close()
# ///////.........//////////////........////////////...........////////////////////////////.............../////



# f = open("demo.txt", "a")

# data = f.write("\n  what the fuck is it doing")
# print(type(data))
# f.close()

# ////////////..............////////////////...................////////////////////////////...............//////

# d = open("simple.txt", "a")
# y = d.write("hello this waqas")
# print(y)
# print(type(y))
# d.close()
# f = open("simple.txt","w+")
# f.write("abc\n")
# print(f.read())
# f.write("what amazing party was this")
# f.close()
# //////////..............////////////////..............//////////////////////...............///////////////..//

# with open("simple.txt","r") as f:
#     data = f.read()
#     print(data)

# ////////////......../////////////..................///////////////................////////////////.........////

# with open("demo.txt","a+")as w:
#     more = w.write("\nwe had to learn basic of python")
#     print(more)
# ///////////............////////////////.............../////////////////............./////////////............///

import os
os.remove("simple.txt")