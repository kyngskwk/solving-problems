import sys
import copy
from pprint import pprint

sys.stdin = open("input.txt", "r")

dx = [0, -1, 1, 0, 0] #위, 아래, 오른쪽, 왼쪽
dy = [0, 0, 0, 1, -1]

def move(temp, pan, i, j):
    s, d, z = pan[i][j]

    if d == 1 or d == 2:
        s = s % ((R-1) * 2)
    else:
        s = s % ((C-1) * 2)

    for fish in range(s):
        if pan[i + dx[d]][j + dy[d]] == -1:
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            else: d = 3

        i += dx[d]
        j += dy[d]

        # 이미 있는 경우
    if temp[i][j] != 0:
        if temp[i][j][2] < z:
            temp[i][j] = [s, d, z]
    else:
        temp[i][j] = [s, d, z]
    # pprint(temp)



R, C, M = map(int, input().split())
k = [[-1] + [0] * (C) + [-1] for _ in range(R)]
k = [[-1] * (C+2)] + k + [[-1] * (C+2)]
pan = copy.deepcopy(k)

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    pan[r][c] = [s, d, z]

ans = 0
man = 1
while man <= C:
    for i in range(1, R+1):
        if pan[i][man] != 0:
            ans += pan[i][man][2]
            pan[i][man] = 0
            break

    temp = copy.deepcopy(k)
    for i in range(1, R+1):
        for j in range(1, C+1):
            if pan[i][j] != 0:
                move(temp, pan, i, j)

    pan = temp
    man += 1

print(ans)

