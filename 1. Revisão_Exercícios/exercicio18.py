a = [1, 2, 3, 4]
b = [0, 0, 0, 0]

for x in range(4):
    b[3 - x] = a[x]

print(b)
