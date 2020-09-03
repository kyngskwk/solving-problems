from pprint import pprint
# key 회전
def chang(key, M):
    new_key = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M-1-i] = key[i][j]
    return new_key

# 맞게 맞물렸는지 체크하기
def checking(ex_pan, M, N):
    # pprint(ex_pan)
    for x in range(M-1, M-1+N):
        for y in range(M-1, M-1+N):
            if ex_pan[x][y] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    ex_pan = [[0] * ((M-1) + N + (M-1)) for _ in range((M-1) + N + (M-1))]
    for idx in range(N):
        ex_pan[M-1+ idx][M-1:M-1+N] = lock[idx]
    # pprint(ex_pan)
    # 시작점 찾기
    for i in range(M-1+N):
        for j in range(M-1+N):
            # print(i, j)
            # 키 채우기
            for _ in range(4):
                key = chang(key, M)
                for key_x in range(M):
                    for key_y in range(M):
                        ex_pan[i + key_x][j + key_y] += key[key_x][key_y]

                if checking(ex_pan, M, N):
                    answer = True
                    return answer
                else:
                    for key_x in range(M):
                        for key_y in range(M):
                            ex_pan[i + key_x][j + key_y] -= key[key_x][key_y]

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))