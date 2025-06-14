# # print("Start....")
# # x = 10

# # y = 20

# # # z = x + y

# # if y < 10:

# #     z = x / y

# # else:
# #     z = x + y

# # print(z)

# # print("End") 

# # try:
# #     if y < 10:

# #      z = x / y
# # except:
# #     print
# #     else:
# #      z = x + y
 
# # print(z)


# # print("End") 


# x = 10

# y = 20
# try:
    
#    if y < 10:
#        z = x / y
#    else:
#      z = x + y + a

#    print(z)
# except ZeroDivisionError as e:

#   print("ZeroDivisionError",e)

# except NameError as e:
#    print("NameError",e)

# else:
#    print("else of try")


# finally:
#    print("In finally block ")




# /////////////\\\\\\/////\\\////\\\\////\\\\///\\\\\/////............\\\\\\\\////////////\\\\\\.....\\\\///////


marks = int(input("Enter your marks ::"))

total_marks = 1100
print("Start")
try:
   if marks < 900:
    avg= (marks / total_marks) * 100
    if marks <= 700:
        print("Normal Grade")
        if avg < 70:
           print("low percentage")
except:
   if marks > 900:
      avg  = (marks / total_marks) * 100
      if avg <= 80:
         print("High percentage")


print(avg)
