def solution(k, room_number):
    answer = []
    for idx in room_number:
        if idx not in answer:
            answer.append(idx)
        else:
            while 1:
                idx += 1
                if idx not in answer:
                    answer.append(idx)
                    break
    return answer

# 효율성...............
hash = {}
def findroom(idx):
    global hash
    idx += 1
    if idx not in hash:
        hash[idx] = 1
        return
    else:
        findroom(idx)

def solution(k, room_number):
    global hash
    answer = []
    for num in room_number:
        if num not in hash:
            hash[num] = 1
        else:
            findroom(num)

    for key in hash.keys():
        answer.append(key)
    return answer

print(solution(10, [1,3,4,1,3,1]))