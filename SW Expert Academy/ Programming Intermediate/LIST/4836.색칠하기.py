import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    nums = int(input())
    blocks = [[0 for j in range(10)] for k in range(10)]
    color_p = 0

    for num in range(nums):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        for f in range(r1, r2+1):
            for s in range(c1, c2+1):
                if blocks[f][s] == 0:
                    blocks[f][s] = color
                if blocks[f][s] != color:
                    blocks[f][s] = 3
                    color_p += 1

    print('#{} {}'.format(tc, color_p))