todos = ['work', 'exercise', 'school']
print("Hello, this is your list.")
print(todos)
# list is printed all the user has to do is add and remove.
start = ""
while True:
    # as long as the loop is true the code will keep on looping.
    start = input("Would you like to add something or remove?: ")
    if start == "add":
        print("Cool! What would you like to add?")
        new = input("")
        todos.append(new)
        # append means to add to the end of the list
        print("This is your new list:")
        print(todos)
    else:
        print("What # of the todo would you like to remove?")
        num = int(input(""))
        num -= 1
        # -= 1 represents the index being taken away by one because the user doesn't know computer binary.
        del todos[num]
        print("This is your new list:")
        print(todos)