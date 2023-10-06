"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for a in range(1, 11):
    print(a)
# Prints all numbers between 1 and 10
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for b in range(900, 1010, 10):
    print(b)
# Starting from 900, it'll count by 10 until it reaches to 1000
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for c in range(1, 100, 9):
    print(c)
# Starts at 1 and begins counting by 9 until 100 is going to be the last number
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
first = range(1,11)
sec = 0
for d in first:
    sec += d
    print(sec)
# variable is set to range, second variable is 0 so every value in the first variable will be added together because of d in first
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5
 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()
# The output is a asterisk on each line and each line gets added a asterisk but only 5 lines. The first for condition makes it so it would only print 5 times then the second for condition is that when star is printed, it would add 1 more to aanother line until the first condition is met which is 5 lines.