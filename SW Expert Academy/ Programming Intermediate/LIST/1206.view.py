case = 10
for i in range(case):
    B = int(input())
    B_list = list(map(int, input().split()))
    cnt = 0
    for k in range(2, B-2):
        if B_list[k] > B_list[k-1] and B_list[k] > B_list[k-2]:
            if B_list[k] > B_list[k+1] and B_list[k] > B_list[k+2]:
                cnt += B_list[k] - max(B_list[k-2], B_list[k-1], B_list[k+1], B_list[k+2])
    print('#{} {}'.format(i+1, cnt))