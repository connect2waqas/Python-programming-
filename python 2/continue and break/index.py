# i = 1
# while i <=5:
#     if i == 3:
#         i +=1
#         break

#     print(i)
#     i +=1

# s1 = "Python Programme"

# for i in s1:
#     if i in "aeiou":
#         continue
#     print(i)
# s1 = "Python Programme"

# for i in s1:
#     if i in " ":
#         break
#     print(i)

sum = 0

while True:
    x = input("enter a number a number or N to exist :")
    if x == "N":
        break
    sum = sum +int(x)

print(sum)
