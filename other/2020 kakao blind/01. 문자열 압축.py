def solution(s):
    length = len(s)
    my_min = 9999999999999
    i = 1
    while i <= length//2 + 1:
        string = s[0:i]
        cnt = 1
        for idx in range(1, length//i):
            start = i*idx
            # print(string, s[start:start+i])
            if string[-i::1] == s[start:start+i]:
                cnt += 1
            else:
                if cnt > 1:
                    string += str(cnt)
                    string += s[start:start+i]
                    cnt = 1
                else:
                    string += s[start:start+i]
                    cnt = 1

        if cnt > 1:
            string += str(cnt)

        sum = len(string) + length % i
        # print(sum)
        my_min = min(my_min, sum)
        i += 1

    return my_min