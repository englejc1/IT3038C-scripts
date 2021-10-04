# A simple calculator script

n1 = int(input('Enter your first number: '))
n2 = int(input('Enter your second number: '))

operator = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

# addition
if operator == "+":
    print('{} + {} = '.format(n1, n2))
    print(n1 + n2)

# subtraction
elif operator == "-":
    print('{} - {} = '.format(n1, n2))
    print(n1 - n2)

# multiplication
elif operator == "*":
    print('{} * {} = '.format(n1, n2))
    print(n1 * n2)

# division
elif operator == "/":
    print('{} / {} = '.format(n1, n2))
    print(n1 / n2)

else:
    print('You did not type a valid operator, please run the script again.')
    quit()