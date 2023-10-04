todos = ['work', 'exercise', 'school']
print("Hello, this is your list.")
print(todos)
start = ""
while True:
    start = input("Would you like to add something or remove?: ")
    if start == "add":
        print("Cool! What would you like to add?")
        new = input("")
        todos.append(new)
        print("This is your new list:")
        print(todos)
    else:
        print("What # of the todo would you like to remove?")
        num = int(input(""))
        num -= 1
        del todos[num]
        print("This is your new list:")
        print(todos)