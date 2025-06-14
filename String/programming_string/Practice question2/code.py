
def operation_list(numeric):
    numeric.append(60)
    numeric.insert(0,5)
    numeric.remove(30)
    print(f"The modified list is: {numeric}")
numeric = [10,20,30,40,50]
operation_list(numeric)

# Input: "apple,banana,cherry"
# Can we input the list then yes 
user_input = input("Enter elements (comma-separated): ")
my_list = user_input.split(",")
print(my_list)  # Output: ["apple", "banana", "cherry"]
# Input: "10 20 30 40 50"

user_input = input("Enter list elements (space-separated): ")
my_list = list(map(str, user_input.split()))
print(my_list)  # Output: [10, 20, 30, 40, 50]
user_input = input("enter list elements (space-separated): ")
my_list = list(map(str,user_input.split()))
print(my_list)


number_of_student = int(input("enter the number of student: "))
entry_list = []
for i in range(number_of_student):
    course_credit = int(input("enter course credit: "))
    entry_list.append(course_credit)
enrollment = []
for i in entry_list:
    if i >= 12:
        enrollment.append("Full-time")
    else:
        enrollment.append("Part-time")
for i in range(number_of_student):
    print(f"Student {i+1} : enrollment - {enrollment[i]}")

number_of_people = int(input("enter number of people: "))
collection = []
for i in range(number_of_people):
    age = int(input("enter age: "))
    collection.append(age)
    print(collection)
childd_count = 0
adult_count = 0
senoir_count = 0
for i in collection:
    if i < 18:
        childd_count +=1
    elif 18 <= i < 65:
        adult_count +=1
    else:
        senoir_count +=1
print(f"The number of child is: {childd_count}")
print(f"The number of adults is: {adult_count}")
print(f"The number of senior is: {senoir_count}")

sentence = input("enter a string: ")
sentence_upper = sentence.upper()
words_list = sentence_upper.split()
modified_sentence = " ".join(words_list)
print(modified_sentence)
print(words_list)
# Here's the Python code to accomplish the task:

# ```
# Step 1: Create a string variable 'sentence' with a chosen sentence
sentence = "Hello, how are you?"

# Step 2: Convert the sentence to upper case
sentence_upper = sentence.upper()

# Step 3: Split the sentence into a list of words
words_list = sentence_upper.split()
print(words_list)
# Step 4: Join the words in the list using a space as a separator
modified_sentence = ' '.join(words_list)

print(modified_sentence)
