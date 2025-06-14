responses = ["Yes","","No","","Maybe","","Yes","No"]

# first answer 
def empty_responses(responses):
    new_list = []
    for i in responses:
        if i =="Yes":
            new_list.append(i)
        elif i == "No":
            new_list.append(i)
        else:
            responses.remove("")
    print(new_list)
    print(responses)
    
empty_responses(responses)

# second way of solving the question
def survey_reponses(responses):
    clean = []
    for i in responses:
        if i !="":
            clean.append(i)
        else:
            pass
    print(clean)
survey_reponses(responses)

'''def performance(class1,class2):
    class1_average = sum(class1)/len(class1)
    class2_average = sum(class2)/len(class2)
    print(f"The performance of class 1 is: {class1_average}")
    print(f"The performance of class 2 is: {class2_average}")

class1 = [85, 90, 88, 92, 78]
class2 = [75, 82, 80, 85, 79]

performance(class1,class2)'''


# Homeworks question

def concatenation(list1,list2):
    # combolist = list1 + list2
    print(list1.extend(list2))
    # print(combolist)

list1 = [[1,2],[3,4],[5,6]]
list2 = [[7,8],[9,10],[11,12]]   
concatenation(list1,list2)

# Homework question 2

string_list = ["Hello,world!", "Pyhton is Awesom!", "I love coding!"]

def to_newline(string_list):
    s1 = string_list[0]
    s2 = string_list[1]
    s3 = string_list[2]
    print(f"{s1} \n{s2} \n{s3}")
to_newline(string_list)

# Homework 3

numbers = [1,2,3]
numbers.append([4,5])
numbers.append(4)
print(numbers)

words = ["Hello","world!"]
sentence = "".join(words)
print(sentence)