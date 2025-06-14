def check_f0r_word():
    word ="zlearning"

    with open("practice.txt") as f:
     data = f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("Not found")

check_f0r_word()