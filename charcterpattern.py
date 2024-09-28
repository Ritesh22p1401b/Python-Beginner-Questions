n = int(input())
i = 1
char = chr(ord('A') + n - 1)
while i <= n:
    j = 1
    while j <= i:
        charn = chr(ord(char) + j - 1)
        print(charn, end="")
        j += 1
    print()
    a = ord(char)
    b = a - 1
    char = chr(b)
    i += 1