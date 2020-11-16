n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
m.sort()

i = 0
while i < len(m):
    print(m[i])
    i += 1