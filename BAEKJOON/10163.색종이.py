import sys

sys.stdin = open("input.txt", "r")

pan = [[0] * 101 for _ in range(101)]
N = int(input())
for i in range(1, N+1):
    x1, y1, down, right = map(int, input().split())
    for x in range(x1, x1+down):
        for y in range(y1, y1+right):
            pan[x][y] = i


for i in range(1, N+1):
    cnt = 0
    for x in range(101):
        for y in range(101):
            if pan[x][y] == i:
                cnt += 1
    print(cnt)