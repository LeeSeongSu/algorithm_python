import collections

a = input().upper()
c = collections.Counter(a) #Counter함수 사용, items형식으로 출력됨
c_max = []
for i,j in c.items():
    if j == max(c.values()):
        c_max.append(i)
if len(c_max) > 1:
    print('?')
else:
    print(c_max[0])

