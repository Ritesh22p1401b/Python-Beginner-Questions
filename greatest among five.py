a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = int(input('Enter the third number'))
d = int(input('Enter the fourth number'))
e = int(input('Enter the fifth number'))
if a > b:
    x = a
else:
    x = b
if c > d:
    y = c
else:
    y = d
if x > y:
    if x > e:
        print('Greatest number is: {}'.format(x))
    else:
        print('Greatest number is: {}'.format(e))
elif y > e:
    print('Greatest number is: {}'.format(y))
else:
    print('Greatest number is: {}'.format(e))









