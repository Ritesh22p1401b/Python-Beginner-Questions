n = int(input())
i = 1
char = 'A'
while i <= n:
    j = 1
    while j <= i:
        print(char, end='')
        j += 1
    print()
    i += 1
    char = chr(ord("A") + i - 1)
