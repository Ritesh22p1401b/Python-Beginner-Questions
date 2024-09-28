x = int(input('Enter the number:'))
rem = 0
temp = x
if temp!=1:
    while sum!=1 and sum!=2 and sum!=3 and sum!=4 and sum!=5 and sum!=6 and sum!=7 and sum!=8 and sum!=9:
        sum = 0
        while temp > 0:
            rem = temp % 10
            sum = sum+rem
            temp = temp//10
        temp = sum

if sum == 1:
    print('{}-is a Magic Number '.format(x))
else:
    print('{}-is not a Magic Number'.format(x))
