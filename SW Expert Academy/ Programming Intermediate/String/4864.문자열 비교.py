def my_compare(str1, str2):
    i = 0
    j = 0
    while i < N and j < M:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == N: return 1
    else: return 0


case = int(input())
for i in range(case):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    print('#{} {}'.format(i+1, my_compare(str1, str2)))