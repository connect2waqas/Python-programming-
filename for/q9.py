num = 13

is_prime = True

for i in range(2,int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print(num, "is a prime number ")

else:
    print(num, "is not a prime number")