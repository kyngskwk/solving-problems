import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, soso = map(int, input().split())
    matrix = [[0] * N for _ in range(N)] # 0으로 채워진 N * N 배열
    for _ in range(soso): # 소금쟁이 개수만큼 반복문을 돌린다.
       i, j, how = map(int, input().split()) # i는 행, j는 열, how는 방향

        if how == 1: # 방향이 1이면 상
            i -= 6 # 상으로 6칸 움직인다.
            if i >= 0 and i < N: # 6칸 움직인 후의 위치가 메트릭스 안에 있을 수 잇는 위치이니?
                if matrix[i][j] != 1: # 위에 조건이 만족하고 1이 아닌걸 보아하니 아직 아무도 안 앉았꾼.
                    matrix[i][j] = 1 # 그럼 1로 바꿔 주자 !

        elif how == 2: # 이건 하 의 경우
            i += 6
            if i >= 0 and i < N:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1

        elif how == 3: # 이건 좌의 경우
            j -= 6
            if j >= 0 and j < N:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1

        else: # 이건 우의 경우
            j += 6
            if j >= 0 and j < N:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1

    # 포문이 다 돌고 나면 앉을 수 있는 소금쟁이들은 이미 앉은 후

    ans = 0 # 답을 0 으로 두고
    for idx in range(N): # 메트릭스를 한줄씩 돌린다,
        ans += sum(matrix[idx]) # 한 줄 씩 그 합을 더해서 ans 변수에 더한다. 소금쟁이들은 1이라서 합이 결국 갯수!

    print('#{} {}'.format(tc, ans))

