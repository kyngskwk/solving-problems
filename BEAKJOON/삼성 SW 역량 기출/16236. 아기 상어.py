import sys
from collections import deque
import copy
from pprint import pprint

sys.stdin = open("input.txt", "r")


N = int(input())
pan = [[-1] + [0]*N + [-1] for _ in range(N)]
pan = [[-1] * (N+2)] + pan + [[-1] * (N+2)]
v = copy.deepcopy(pan)

for idx in range(1, N+1):
    pan[idx][1:N+1] = list(map(int, input().split()))

queue = deque([])

for i in range(1, N+1):
    for j in range(1, N+1):
        if pan[i][j] == 9:
            pan[i][j] = 0
            queue.append([i, j, 0]) # 좌표, 단계
            v[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

time = 0

fish = []
shark = [2, 0]

while queue:
    flag = 0
    # pprint(v)
    now = queue.popleft()
    x, y, k = now[0], now[1], now[2]
    # 물고기 비교

    if pan[x][y] != 0 and pan[x][y] < shark[0]:
        if len(fish) == 0:
            fish = [x, y, k] # 좌표과 단계(거리, 초)

        else:
            # 멀리 있는 물고기 !
            if k > fish[-1]:
                # 현재 물고기로 처리
                time += fish[-1]
                pan[fish[0]][fish[1]] = 0

                # queue 리셋
                queue = deque([])
                queue.append([fish[0], fish[1], 0])
                # v 리셋
                v = [[-1] + [0] * N + [-1] for _ in range(N)]
                v = [[-1] * (N + 2)] + v + [[-1] * (N + 2)]
                fish = []

                shark[-1] += 1
                # 상어 크기
                if shark[0] == shark[1]:
                    shark = [shark[0] + 1, 0]

                flag = 1

            else:
                if x < fish[0]:
                    fish = [x, y, k]
                elif x == fish[0] and y < fish[1]:
                    fish = [x, y, k]

    if flag == 0:
        for idx in range(4):
            # 일단 갈 수 있는 곳인지 확인
            n_x, n_y = x + dx[idx], y + dy[idx]
            if pan[n_x][n_y] != -1 and pan[n_x][n_y] <= shark[0] and v[n_x][n_y] == 0:
                queue.append([n_x, n_y, k+1])
                v[n_x][n_y] = 1


    if len(queue) == 0 and len(fish) != 0:
        # 현재 물고기로 처리
        time += fish[-1]
        pan[fish[0]][fish[1]] = 0

        # queue 리셋
        queue = deque([])
        queue.append([fish[0], fish[1], 0])
        # v 리셋
        v = [[-1] + [0] * N + [-1] for _ in range(N)]
        v = [[-1] * (N + 2)] + v + [[-1] * (N + 2)]
        fish = []

        shark[-1] += 1
        # 상어 크기
        if shark[0] == shark[1]:
            shark = [shark[0] + 1, 0]



print(time)