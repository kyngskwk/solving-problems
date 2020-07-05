import sys

sys.stdin = open("input.txt", "r")

pan = [[0] * 101 for _ in range(101)]
ans = 0
for tc in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            pan[i][j] = 1

for i in range(101):
    ans += sum(pan[i])
print(ans)