import sys
from pprint import pprint

sys.stdin = open("input.txt", "r")

pan = [[0] * 100 for _ in range(100)]
result = 0
for tc in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            print(i, j)
            pan[i][j] = 1
            print(pan[i][j])

for i in range(1, 100):
    result += sum(pan[i])
print(result)