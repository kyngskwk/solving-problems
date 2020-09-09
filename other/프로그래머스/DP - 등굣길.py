from pprint import pprint

# dx = [1, 0]
# dy = [0, 1]

def solution(m, n, puddles):
    answer = 0
    pan = [[0] * (m+2) for _ in range(n+2)]
    pan[1][1] = 1
    for x in range(1, n+2):
        for y in range(1, m+2):
            if x == n and y == m:
                answer = pan[x-1][y] + pan[x][y-1]
                return answer % 1000000007
            else:
                if [y, x] in puddles:
                    continue
                else:
                    pan[x][y] += pan[x-1][y] + pan[x][y-1]


# dfs
# def going (m, n, x, y, pan, v):
#     global answer
#     pprint(v)
#     if x == n and y == m:
#         answer += 1
#         return
#     else:
#         for idx in range(2):
#             next_x = x + dx[idx]
#             next_y = y + dy[idx]
#             if v[next_x][next_y] == 0 and pan[next_x][next_y] == 0:
#                 v[next_x][next_y] = 1
#                 going(m, n, next_x, next_y, pan, v)
#                 v[next_x][next_y] = 0
#
#
# def solution(m, n, puddles):
#     global answer
#     pan = [[1] * (m+2)] + [[1] + [0] * m + [1] for _ in range(n)] + [[1] * (m+2)]
#     for puddle in puddles:
#         pan[puddle[1]][puddle[0]] = 1
#
#     v = [[0] * (m+2) for _ in range(n+2)]
#     going(m, n, 1, 1, pan, v)
#     return answer % 1000000007

print(solution(4, 3, [[2, 2]]))