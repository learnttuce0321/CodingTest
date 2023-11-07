def solution(s):
    answer = True
    count = 0
    
    for i in s:
        if s[0] == ')' :
            return False
        
        if i == '(':
            count+=1
        elif i == ')' and count == 0:
            return False
        else:
            count-=1
        
    if not count == 0:
        return False
    else :
        return True
