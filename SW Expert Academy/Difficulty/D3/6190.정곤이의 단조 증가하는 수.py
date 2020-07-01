import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = []

    for i in range(1, N):
        for j in range(0, i):
            num = num_list[i] * num_list[j]
            num = str(num)
            for n in range(len(num)-1):
                if num[n] > num[n+1]:
                    break
            else:
                result.append(int(num))

    if len(result) > 0:
        ans = sorted(result)[-1]
    else:
        ans = -1

    print('#{} {}'.format(tc, ans))
