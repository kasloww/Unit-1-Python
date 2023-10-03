todos = []
print("Hello, would you like to add something to your to-do list? Y/N")
start = input("")
if start == "y" or "Y":
    print("Cool! What would you like to add?")
else:
    print("Okay.")
new = input("")
todos.append(new)
print("Okay, your list is: ")
print(todos)
print("Do you want to add or remove something from the list?")
gone = input("")
if gone == "remove":
    print("Alright which # of the todo do you want to remove?")
    num = int(input(""))
    del todos[num]
    print("Okay, your new list is:")
    print(todos)
elif gone == "add":
    print("Alright, what else do you want to add?")
else:
    print("Okay. Safe")