"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
kas = ['iphone', 'airpods', 'watch', 'wallet']
print(kas)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
kas.append('music')
print(kas)
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
kas.remove('watch')
print(kas)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
kas[3] = "drake"
print(kas)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
kas.append('sza')
kas.append('jaydes')
kas.append('brent')
print(kas)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del kas[5]
print(kas)
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
rnb = (kas[0:2])
print(rnb)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
kaslovesrnb = kas + rnb
print(kaslovesrnb)