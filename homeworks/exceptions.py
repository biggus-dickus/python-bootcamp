#! /usr/bin/env python

# Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print(f'Incorrect argument provided: expected integer or float, got {type(i)} instead.')  

# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
def divide(x, y):
    result = 0
    
    try:
        result = x/y
    except ZeroDivisionError:
        print('You can\'t divide by zero, you know.')
    finally:
        print('All done')      

    return result

print(divide(5, 5))

# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.
def square_number():
    result = 0

    while True:
        num = input('Enter a number ')
        
        try:
            result = int(num) ** 2
            return result
        except:
            print('Invalid input!')
        else:
            break

res = square_number()

print(res)
