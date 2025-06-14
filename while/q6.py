word = input("enter a string ").lower()

count = 0
vowels ="aeiou"
index= 0

while index < len(word):
    if word[index] not in vowels and word[index].isalpha():
        count +=1
        
    index +=1
print(f"Number of consonaints {count}")