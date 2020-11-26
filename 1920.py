import sys

N = int(sys.stdin.readline())
x = list((map(int,sys.stdin.readline().split())))

M = int(sys.stdin.readline())
y = list(map(int,sys.stdin.readline().split()))

for i in y:
    if i in x:
        print(1)
    else:
        print(0)
