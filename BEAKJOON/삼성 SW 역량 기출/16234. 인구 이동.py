import sys

sys.stdin = open("input.txt", "r")

cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find(pan, i, j, v):
    global temp
    for idx in range(4):
        n_x = i + dx[idx]
        n_y = j + dy[idx]
        if L <= abs(pan[i][j] - pan[n_x][n_y]) <= R and pan[n_x][n_y] >= 0:
            if v[n_x][n_y] == 0:
                v[n_x][n_y] = 1
                temp.append([n_x, n_y])
                find(pan, n_x, n_y, v)


N, L, R = map(int, input().split())
pan = [[-1] * (N+2) for _ in range(N+2)]
for idx in range(1, N+1):
    pan[idx][1:N+1] = list(map(int, input().split()))

print(pan)
temp = []
while True:
    v = [[0] * (N + 2) for _ in range(N + 2)]
    flag = 0
    for i in range(1 + N+1):
        for j in range(1 + N+1):
            if v[i][j] == 0 and pan[i][j] >= 0:
                v[i][j] = 1
                temp = [[i, j]]
                find(pan, i, j, v)

            if len(temp) > 1:
                flag = 1
                pp = 0
                for t in temp:
                    pp += pan[t[0]][t[1]]
                for k in temp:
                    pan[k[0]][k[1]] = pp // len(temp)

    if flag == 0:
        break
    else:
        cnt += 1


print(cnt)





