print('Welcome to my Calculator!')
num1 = float(input("Enter a number: "))
num2 = float(input("Now enter a second number: "))
# user chooses 2 numbers to begin with
print('What do you want to do with these numbers?')
print('1. Add 2. Subtract 3. Multiply 4. Divide 5. Floor Divide 6. Exponential 7. Remainder')
choice = int(input(""))
# whatever number they choose between 1-7 it'll give them a operation
if choice == 1:
    print("Here is your answer:") 
    print(num1 + num2)
elif choice == 2:
    print("Here is your answer:")
    print(num1 - num2)
elif choice == 3:
    print("Here is your answer:")
    print(num1 * num2)
elif choice == 4:
    print("Here is your answer:")
    print(num1 / num2)
elif choice == 5:
    print("Here is your answer:")
    print(num1/num2)
elif choice == 6:
    print("Here is your answer:")
    print(num1 ** num2)
elif choice == 7:
    print("Here is your answer:")
    print(num1 % num2)
