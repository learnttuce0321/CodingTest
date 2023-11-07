def solution(phone_book):
    answer = True
    
    sorted_phone_book = sorted(phone_book)
    
    for i in range(len(sorted_phone_book) - 1):
        if sorted_phone_book[i] == sorted_phone_book[i+1][0:len(sorted_phone_book[i])]:
            return False

    return answer