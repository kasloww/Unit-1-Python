import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import datetime
thedate = 2023, 10, 11
thetime = 10, 24, 54
print("Date and Time:", thedate, thetime) 
"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
every = datetime.now()
print("every.strftime(%m/%d/%Y,%X")
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""