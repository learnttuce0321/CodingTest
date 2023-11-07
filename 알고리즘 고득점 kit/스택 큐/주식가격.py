def solution(prices):
    answer = []
    print(prices)

    for i in range(len(prices)):
        count = 1
        static_price = prices[i]

        for j in range(i+1,len(prices)):
            if static_price <= prices[j] and not j == (len(prices) - 1):
                count += 1
            else:
                answer.append(count)
                break
                
    answer.append(0)
    return answer
