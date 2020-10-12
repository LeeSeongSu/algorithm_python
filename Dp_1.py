# 첫째 줄에 식량창고의 개수 N
# 둘째 줄에 식량의 개수K
# 얻을 수 있는 식량의 최댓값, 단 연속된 창고를 이용할 순 없음

n = int(input())
array = list(map(int,input().split()))

dp = [0]*100

dp[0] = array[0]
dp[1] = max(array[0],array[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+array[i])

print(dp[n-1])