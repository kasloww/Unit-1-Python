try:
    age = int(input('Enter your age: '))
except:
   print("Type out the actual number")
# This is where one of the erros occurs, prints a statement when conditions not met
try: 
    faveNum = int(input('What is your favorite number: '))
except:
   ("Don't put 0, 0 can't be divided.")
if age <= 21:
    print('You are not allowed to enter, you are too young.')
else:
    print('Welcome, you are old enough.')

print("Type out the actual number instead of letters.")

print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
