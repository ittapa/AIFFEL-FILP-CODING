def solution(prices):
    answer = []
    for idx in range(len(prices)-1):
        count = 0
        for a in range(idx, len(prices)-1):
            if prices[idx] <= prices[a]:
                count = count + 1
            else :
                break
        answer.append(count)
    answer.append(0)
    return answer

t1  =[1, 2, 3, 2, 3]



def solution2(prices):
    answer =[]
    L = len(prices)
    for idx in range(L):
        a = prices.pop()
        print(a)


    return answer


print(solution2(t1))