x = int(input('enter the first number'))
y = int(input('enter the second number'))
z = int(input('enter the third number'))
if x > y:
    if x > z:
        print('greatest number is:{}' .format(x))
    else:
        print('greatest number is:{}' .format(z))
elif y > z:
    print('greatest number is:{}'.format(y))
else:
    print('greatest number is:{}'.format(z))








