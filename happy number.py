def x(n):
    res = rem = 0
    while n > 0:
        rem = n % 10
        res = res + (rem * rem)
        n = n // 10
    return res


n = int(input('Enter the number:'))
result = n
while result != 1 and result != 4:
    result = x(result)
if result == 1:
    print('{} is a happy number'.format(n))
else:
    print('{} is unhappy number'.format(n))
