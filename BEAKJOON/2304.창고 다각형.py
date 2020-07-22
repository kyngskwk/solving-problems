import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
line = [0] * 1001
max_i, max_h = 0, 0
for tc in range(N):
    idx, h = map(int, input().split())
    line[idx] = h
    if h >= max_h:
        max_h = h
        max_i = idx

for idx in range(1, max_i):
    if line[idx] >= line[idx+1]:
        line[idx+1] = line[idx]

for idx in range(-1, -(1001-max_i), -1):
    if line[idx] >= line[idx-1]:
        line[idx-1] = line[idx]

print(sum(line))