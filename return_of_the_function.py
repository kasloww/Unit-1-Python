"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def sqre(x): 
    return x**2
print (sqre(10))
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def lew(a, b):
    return a * b

c = lew(6, 10)
print(c)
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def temp(c):
    return (c *(10/2)) + 30
print(temp(1),"C")
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def aver(d):
    total = sum(d)
    avg = total / len(d)
    return avg
print(aver([1,2,3,4,5,6,7,8,9,10]))