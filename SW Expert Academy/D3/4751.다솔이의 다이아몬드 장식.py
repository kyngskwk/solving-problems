import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    word = list(input())
    N = 4 * len(word) + 1
    ans = [['.'] * N for _ in range (N)]

    for i in range(0, N-1, 2):
        ans[1][i+1] = '#'
        ans[3][i+1] = '#'
        ans[2][i] = '#'
    ans[2][-1] = '#'

    idx = 0
    for i in range(2, N, 4):
        ans[0][i] = '#'
        ans[2][i] = word[idx]
        idx += 1
        ans[4][i] = '#'

    for _ in range(5):
        print(''.join(ans[_]))