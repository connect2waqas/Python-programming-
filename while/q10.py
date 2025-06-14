string = input("enter a string = ")
chr_to_count = input("enter character to be count = ")
index = 0
count = 0

while index < len(string):
    if string[index] == chr_to_count:
        count +=1
    index +=1
print(f'{chr_to_count} = {count}')