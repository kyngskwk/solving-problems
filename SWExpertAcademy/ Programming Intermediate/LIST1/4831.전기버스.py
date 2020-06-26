import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    oil_stop = list(map(int, input().split()))

    bus, oil, go = 0, 0, K

    while bus != N:
        if (bus + go) >= N:
            break

        for go in range(K, 0, -1):
            if (bus + go) in oil_stop:
                oil += 1
                bus += go
                go = K
                break
        else:
            oil = 0
            break

    print('#{} {}'.format(tc, oil))