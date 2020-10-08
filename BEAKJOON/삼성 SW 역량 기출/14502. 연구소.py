import copy
import sys
from pprint import pprint

sys.stdin = open('input.txt', 'r')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
my_max = 0

### 바이러스 퍼지는 함수
def virus(pan, i, j, N, M):
    # pprint(pan)
    global my_min
    for idx in range(4):
        next_x = i + dx[idx]
        next_y = j + dy[idx]
        if pan[next_x][next_y] == 0:
            pan[next_x][next_y] = 2
            virus(pan, next_x, next_y, N, M)


### 벽 세우는 함수
def wall(pan, cnt, N, M):
    global my_max
    if cnt == 3:
        temp_pan = copy.deepcopy(pan)
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if pan[i][j] == 2:
                    virus(temp_pan, i, j, N, M)

        # pprint(temp_pan)
        # 0 개수 세기
        cnt = 0
        # pprint(temp_pan)
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if temp_pan[i][j] == 0:
                    cnt += 1

        my_max = max(cnt, my_max)
        return

    else:
        for i in range(1, N+1):
            for j in range(1, M+1):
                if pan[i][j] == 0:
                    pan[i][j] = 1
                    wall(pan, cnt+1, N, M)
                    pan[i][j] = 0


N, M = map(int, input().split())
pan = [[1] * (M+2) for _ in range(N+2)]
for idx in range(1, N+1):
    pan[idx][1:M+1] = list(map(int, input().split()))


for i in range(1, N+1):
    for j in range(1, M+1):
        if pan[i][j] == 0:
            pan[i][j] = 1
            wall(pan, 1, N, M)
            pan[i][j] = 0

print(my_max)