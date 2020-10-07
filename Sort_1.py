# 두 배열 A,B
# 최 대 k 번 바꿔치기 연산 가능
# A의 모든 원소의 합이 최대가 되도록 하자.
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))
