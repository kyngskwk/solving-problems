import sys
import copy
from pprint import pprint

sys.stdin = open("input.txt", "r")

dx = [0, -1, 1, 0, 0] #위, 아래, 오른쪽, 왼쪽
dy = [0, 0, 0, 1, -1]

def move(temp, pan, i, j):
    print(i, j)
    s, d, z = pan[i][j]

    # if d == 1:
    #     i += s
    #     if i > R:
    #         i += i//R
    #         rot , next_i = i//R, i%R
    #         # 넘으면 방향 바꾸기
    #         if rot % 2 == 1:
    #             d = 2
    #             i = next_i
    #         else:
    #             i = R - next_i + 1
    #
    # elif d == 2:
    #     i += s
    #     if i > R:
    #         i += i//R
    #         rot , next_i = i//R, i%R
    #         # 넘으면 방향 바꾸기
    #         if rot % 2 == 1:
    #             d = 1
    #             i = R - next_i + 1
    #         else:
    #             i = next_i
    #
    # elif d == 3:
    #     j += s
    #     if j > C:
    #         j += j//C
    #         rot , next_j = j//C, j%C
    #         # 넘으면 방향 바꾸기
    #         if rot % 2 == 1:
    #             d = 4
    #             j = next_j
    #         else:
    #             j = R - next_j + 1
    #
    # elif d == 4:
    #     j += s
    #     if j > C:
    #         j += j//C
    #         rot , next_j = j//C, j%C
    #         # 넘으면 방향 바꾸기
    #         if rot % 2 == 1:
    #             d = 3
    #             j = R - next_j + 1
    #         else:
    #             j = next_j

    # 시간 초
    if d in [1, 2]:
        i += s
        while i > R:
            i += 1
            i -= R
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            elif d == 4:
                d = 3

    if d == 1

    for fish in range(s):
        if pan[i+dx[d]][j+dy[d]] == -1:


        i += dx[d]
        j += dy[d]

    # 이미 있는 경우
    if temp[i][j] != 0:
        if temp[i][j][2] < z:
            temp[i][j] = [s, d, z]
    else:
        temp[i][j] = [s, d, z]
    pprint(temp)



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

