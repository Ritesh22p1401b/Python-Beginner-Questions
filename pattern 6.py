x = int(input('Enter the number of row:'))
for i in range(x):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,x):
        print('* ',end='')
    print()
for i in range(x):
    for j in range(i,x-1):
        print(' ',end='')
    for j in range(i+2):
        print('* ',end='')
    print()