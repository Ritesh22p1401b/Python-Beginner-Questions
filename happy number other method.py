x = int(input('Enter the number:'))
temp = x
while sum != 1 and sum != 4:
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum+rem*rem
        temp = temp//10
    temp = sum
if sum == 1:
    print('{}-is a Happy Number'.format(x))
else:
    print('{}-is an Unhappy Number.'.format(x))
