x = int(input('Enter the upper value:'))
y = int(input('Enter the lower value:'))
a = 0
if y >= 10 and x >= 10:
    for i in range(x, y+1):
        temp = i
        rev = 0
        while temp > 0:
            rem = temp % 10
            rev = rev*10+rem
            temp = temp//10

        if rev == i:
            print(i)
            a += 1
    print('Number between {} and {} is-{}'.format(x, y, a))
else:
    print('please enter two digit number for checking palindrome in first and last value')

