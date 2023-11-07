def solution(priorities, location):
    answer = 1
    temp_l = location
    temp_p = priorities.copy()

    while not len(temp_p) == 0 and not temp_p.index(max(temp_p)) == temp_l:
        high_p_index = temp_p.index(max(temp_p))

        for _ in range(high_p_index):
            temp = temp_p.pop(0)
            temp_p.append(temp)
            temp_l -= 1

            if temp_l == -1:
                temp_l = len(temp_p) - 1

        temp_p.pop(0)
        temp_l -= 1
        answer += 1

    return answer
