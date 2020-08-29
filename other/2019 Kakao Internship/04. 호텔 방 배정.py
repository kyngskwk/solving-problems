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
def solution(k, room_number):
    room_dict = {}
    answer = []
    for num in room_number:
        n = num
        visit = [n]
        while n in room_dict:
            n = room_dict[n]
            visit.append(n)
        answer.append(n)
        for v in visit:
            room_dict[v] = n+1
    return answer

# 다른 코드
def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        print(num)
        number = room.get(num, 0)
        if number != 0:
            temp = [num]
            while True:
                index = number
                number = room.get(number, 0)
                print(number, room)
                if number == 0:
                    answer.append(index)
                    room[index] = index + 1
                    for i in temp:
                        room[i] = index + 1
                    break
                temp.append(number)
        else:
            answer.append(num)
            room[num] = num + 1
    return answer

print(solution(10, [1,3,4,1,3,1]))