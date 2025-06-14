# Input a number from the user
num = int(input("Enter a number: "))

# Prime check logic
if num > 1:  # A number less than or equal to 1 cannot be prime
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to √num
        if num % i == 0:  # If divisible by any number other than 1 and itself
            print(f"{num} is not a prime number.")
            break
    else:  # This runs if no divisors are found (loop completes without breaking)
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
