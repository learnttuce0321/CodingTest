import math

def solution(arr):
    answer = [arr[0]]
    temp = arr[0]    

    for i in arr:
        if i!= temp:
            temp = i
            answer.append(temp)
            continue
        else:
            continue
    return answer