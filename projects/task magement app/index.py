# def task():
#     tasks = []
#     print("<-----Welcome to task mangement app ")
#     total_task= int(input("how many task you to add = "))
#     for i in range(1, total_task +1):
#         task_name = input(f"enter your task {i} = ")
#         tasks.append(task_name)
    
#     print(f"Today's task are : \n {tasks}")
#     while True:
#         operation = int(input("enter \n1-add\n2-update\n3-delete\n4-view\n5-Exit/stop"))
#         if operation == 1:
#             add = input("enter task you want to add = ")
#             tasks.append(add)
#             print(f"Task {add} has been successfully added...")
#         elif operation == 2:
#             updated_val = input("enter task you want to update = ")
#             if updated_val in tasks:
#                 up = input("enter new task = ")
#                 ind = tasks.index(updated_val)
#                 tasks[ind] = up
#                 print(f"update task {up}")
#         elif operation == 3:
#             del_val= input("enter task to delete =")
#             if del_val in tasks:
#                 tasks.remove(del_val)
#                 print(f"Task {del_val} has been deleted..")
#         elif operation == 4:
#             print(f"Total task is = {tasks} ")

#         elif operation == 5:
#             print("program closing...")
#             break
        
#         else:
#             print("invalid input")





# task()

# def task():
#     tasks = []
#     print("<----Welcome to task mangement app ")
#     total_task = int(input("How many task want to add = "))
#     for  i in range(1, total_task + 1):
#         task_name = input(f"enter your task {i} ")
#         tasks.append(task_name)

#     print(f"Today's total tasks are : \n {tasks}")
#     while True:
#         operaiton = int(input("Enter \n1-add\n2-update\n3-delete\n4-view\n5-Exist/stop."))
#         if operaiton == 1:
#             add = input("enter task you want to added ")
#             tasks.append(add)
#             print(f"Task {add} has been successfully added..")
#         elif operaiton == 2:
#             update_val = input("enter the task to update = ")
#             if update_val in tasks:
#                 up = input("enter new task = ")
#                 ind = tasks.index(update_val)
#                 tasks[ind] = up
#                 print(f" {up} update task  ")
#             else:
#                 print("No value found")
#         elif operaiton == 3:
#             del_val = input("enter the task to deleted  = ")
#             if del_val in tasks:
#                 tasks.remove(del_val)
#                 print(f"Task {del_val} has been deleted")
#             else:
#                 print("No value found")
        
#         elif operaiton == 4:
#             print(f"Total; is =  {tasks}")
        
#         elif operaiton == 5:
#             print("Closing the program...")
#             break
#         else:
#             print("invalid input")



# task()

#  after we should see the code again for more better understanding
