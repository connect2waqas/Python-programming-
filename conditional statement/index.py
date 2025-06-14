# # age =12
# # if(age>=18):
# #     print("you can vote and also apply for license")
# light="red"
# if(light =="green"):
#     print("go")
# elif(light =="red"):
#     print("stop")
# elif(light =="other"):
#     print("wait")
age = int(input("enter your age for votting:"))
if(age >=18):
    if(age >=80):
        print("cannot vote")
    else:
        print("can vote")
else:
    print("cannot vote")