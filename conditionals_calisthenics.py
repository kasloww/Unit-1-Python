'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
num = int(input("Enter a number: "))
if num > 10 and num % 2 == 0:
    print("True")
    # if the user enters a number greater than 10 and even, then it'll be true otherwise false
else:
    print("False")
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = int(input("What is your age?: "))
status = input("Are you a student? Respond yes or no: ")
if age < 18 or status == "yes":
    print("Your ticket is $10.")
else:
    print("Your ticket is $20.")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits = ['watermelon', 'apples', 'oranges', 'cantaloupes']
response = input("Enter a fruit name: ")
if response == fruits:
    print("That fruit is in the list!")
else:
    print("That isn't in the list.")
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
years = int(input("Enter a year: "))
if years % 100 and years % 4 == 0:
    print("That is a century and a leap year.")
else:
    print("That is not a leap year")
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''