import sys
import copy

sys.stdin = open("input.txt", "r")


dx = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽,
dy = [1, 0, -1, 0]

def cctv(i, j, dir, pan):
    while pan[i][j] != -1 and pan[i][j] != 6:
        i += dx[dir]
        j += dy[dir]
        if pan[i][j] == 0:
            pan[i][j] = '#'
    return


def find(q, pan, idx):
    global cnt
    if idx == len(q):
        c = 0
        for x in range(1, N+1):
            for y in range(1, M+1):
                if pan[x][y] == 0:
                    c += 1
        cnt = min(cnt, c)
        return

    num, i, j = q[idx]
    if num == 1:
        for dir in range(4):
            temp_pan = copy.deepcopy(pan)
            cctv(i, j, dir, temp_pan)
            find(q, temp_pan, idx+1)

    elif num == 2:
        for dir in range(2):
            temp_pan = copy.deepcopy(pan)
            cctv(i, j, dir, temp_pan)
            cctv(i, j, dir+2, temp_pan)
            find(q, temp_pan, idx+1)

    elif num == 3:
        for dir in range(4):
            temp_pan = copy.deepcopy(pan)
            cctv(i, j, dir, temp_pan)
            cctv(i, j, (dir+1) % 4, temp_pan)
            find(q, temp_pan, idx+1)

    elif num == 4:
        for dir in range(4):
            temp_pan = copy.deepcopy(pan)
            cctv(i, j, dir, temp_pan)
            cctv(i, j, (dir + 1) % 4, temp_pan)
            cctv(i, j, (dir + 2) % 4, temp_pan)
            find(q, temp_pan, idx+1)

    elif num == 5:
        temp_pan = copy.deepcopy(pan)
        for dir in range(4):
            cctv(i, j, dir, temp_pan)
        find(q, temp_pan, idx+1)



N, M = map(int, input().split())
pan = [[-1] * (M+2) for _ in range(N+2)]
for idx in range(1, N+1):
    pan[idx][1:M+1] = list(map(int, input().split()))

cnt = 9999999999999
q = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if pan[i][j] >= 1 and pan[i][j] != 6:
            q.append([pan[i][j], i, j])

find(q, pan, 0)
print(cnt)