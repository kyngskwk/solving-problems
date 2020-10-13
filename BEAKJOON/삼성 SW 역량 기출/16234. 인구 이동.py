import sys

sys.stdin = open("input.txt", "r")

cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
temp = []

def find(pan, i, j, v):
    global temp
    if


N, L, R = map(int, input().split())
pan = [[-1] * (N+2) for _ in range(N+2)]
for idx in range(1, N+1):
    pan[idx][1:N+1] = list(map(int, input().split()))

v = [[0] * (N+2) for _ in range(N+2)]



# def gap(pan, i, j, v, L, R):
#     global cnt, temp, pp
#
#     for idx in range(4):
#         pgap = abs(pan[i+dx[idx]][j+dy[idx]] - pan[i][j])
#         if pgap >= L and pgap <= R and v[i+dx[idx]][j+dy[idx]] == 0 and pan[i+dx[idx]][j+dy[idx]] >= 0:
#             v[i + dx[idx]][j + dy[idx]] = 1
#             gap(pan, i+dx[idx], j+dy[idx], v, L, R)
#             pp += pan[i+dx[idx]][j+dy[idx]]
#             temp.append((i+dx[idx], j+dy[idx]))
#
#
# N, L, R = map(int, input().split())
# pan = [[-1] * (N+2) for _ in range(N+2)]
# for idx in range(1, N+1):
#     pan[idx][1:N+1] = list(map(int, input().split()))
#
#
# v = [[0] * (N+2) for _ in range(N+2)]
# while True:
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if v[i][j] == 0:
#                 pp = pan[i][j]
#                 temp = [(i, j)]
#                 gap(pan, i, j, v, L, R)
#                 if len(temp) > 1:
#                     cnt += 1
#                     print(temp)
#                     change = pp // len(temp)
#                     for p, q in temp:
#                         pan[p][q] = change
#
#     if len(temp) == 1:
#         break



print(cnt)





