"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
a = 1
while a > 0:
    print(a)
    a += 1
    if a == 11:
        break
# I wanted to display numbers 1-10 and since 1 is greater than 0, I made it so it'll add 1 everytime variable "a" is printed and when it reaches to a certain number it'll break
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
b = 10
while b > 0:
    print(b)
    b -= 1
# since it's counting down, it doesn't need to break to a certain number. So I made it so it will print a and take away 1 from it 
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
c = int(input('Give me a number: '))
d = 1
while c > 0:
    d += c
    c -= 1
    print(d)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
passw = input('Im thinking of a password. Try to guess it: ')
actual = "apple"
while passw != actual:
    print("Try to think of a red fruit.")
    break
else:
    print('Your right.')
# Made a variable for the input of the user and a another variable for the password it has to be. Made a while loop so if it's not equal to the set password, it will print a hint towards the right password and to try again.
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""