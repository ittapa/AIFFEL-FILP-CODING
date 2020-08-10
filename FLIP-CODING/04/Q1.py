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

print(solution(t1))

def solution2(prices):
    answer = []

    for p in prices:

        print(prices.pop(-1) #


    return answer

solution2(t1)
