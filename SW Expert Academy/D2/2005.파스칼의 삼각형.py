import sys

sys.stdin = open('input.txt', 'r')

def pascal(num):
    result = [[1 for i in range(j)] for j in range(1, num+1)]
    if num >= 3:
        for x in range(2, num):
            for y in range(1, x):
                result[x][y] = result[x-1][y-1] + result[x-1][y]
    return result

case = int(input())
for i in range(case):
    print('#{}'.format(i+1))
    num = int(input())
    for lst in pascal(num):
        print(' '.join(map(str,lst)))