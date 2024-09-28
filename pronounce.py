s = input()
s1 = "aeiou"
count = 0
for i in s:
    if i not in s1:
        count += 1
    else:
        if count >= 4:
            pass
        else:
            count = 0
print(count)
