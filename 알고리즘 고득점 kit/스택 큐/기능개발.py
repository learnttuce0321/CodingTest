import math

def solution(progresses, speeds):
    answer = []
    temp = []
    count = 0
    
    rest = [100-i for i in progresses]
    rest_day = [math.ceil(rest[i]/speeds[i]) for i in range(len(speeds))]
    
    
    while(len(rest_day)):
        rest_day = [rest_day[i] - rest_day[0] for i in range(len(rest_day))]
        
        while(len(rest_day) and rest_day[0] <= 0):
            rest_day.pop(0)
            count+=1
        
        answer.append(count)
        count = 0    

    return answer