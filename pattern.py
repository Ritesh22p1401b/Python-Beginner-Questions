x = int(input('Enter the row:'))
for i in range(x):
    for j in range(i,x):
        print('* ',end='')
    for j in range(i):
        print('  ',end='')
    for j in range(i):
        print('  ',end='')
    for j in range(i,x):
        print('* ',end='')
    print()
