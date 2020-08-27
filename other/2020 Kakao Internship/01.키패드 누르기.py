
def solution(numbers, hand):
    answer = ''
    l_x, l_y = 3, 0
    r_x, r_y = 3, 2

    i, j = 0, 0
    l_distance, r_distance = 0, 0

    for num in numbers:
        j = num % 3 - 1
        if num != 0 and j == -1: j = 2

        if j == 2: i = nu m/ /3 - 1
        else: i = num // 3

        if num != 0 and j == 0:
            l_x, l_y = i, j
            answer += 'L'

        elif num != 0 and j == 2:
            r_x, r_y = i, j
            answer += 'R'

        else:
            if num == 0:
                i, j = 3, 1

            l_distance = abs(l_x - i) + abs(l_y - j)
            r_distance = abs(r_x - i) + abs(r_y - j)

            if l_distance < r_distance:
                l_x, l_y = i, j
                answer += 'L'

            elif l_distance > r_distance:
                r_x, r_y = i, j
                answer += 'R'

            else:
                if hand == 'left':
                    l_x, l_y = i, j
                    answer += 'L'

                else:
                    r_x, r_y = i, j
                    answer += 'R'

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
