print('**********************')
print("     Calculator")
print('**********************')
i = input('Whats your name? ')
print('Hello ' + i)

while True:
    print('1 - Add')
    print('2 - Subtract')
    print('3 - Multiply')
    print('4 - Divide')
    cal = input('What calculation do you want? ')
    a = input('Enter first number: ')
    b = input('Enter second number: ')
    if cal == 1:
        print(i + ', the total is: ' + (int(a) / int(b)))
    elif cal == 2:
        print(i + ', the total is: ' - (int(a) / int(b)))
    elif cal == 3:
        print(i + ', the total is: ' * (int(a) / int(b)))
    elif cal == 4:
        print(i + ', the total is: ' + (int(a) / int(b)))
    print('')
    x = input('Press q to quit, otherwise continue ')
    if x.lower() == 'q':
        break
    else:
        print('')
        continue