import heapq
import sys

input = sys.stdin.readline

N = int(input().strip())
array = []

for i in range(N):
    x = int(input().strip())
    if x == 0:
        if array:
            print(-heapq.heappop(array))
        else: print(0)
    else: heapq.heappush(array, -x)


