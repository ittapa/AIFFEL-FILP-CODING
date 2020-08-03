# h-index
'''

어떤 과학자가 발표한 논문 n편 중,
h번 이상 인용된 논문이 h편 이상이고 나
머지 논문이 h번 이하 인용되었다면 h의 최댓값이
이 과학자의 H-Index입니다.\\
n 편
h 번 이상 인용 논문이 h 개,
// 나머지는 h 번 이하 인용

정렬 내림차순
N-h

최댓값 max
'''

def solution(citations):

    citations.sort(reverse=True) #내림차순
    print(citations)
    N = len(citations)

    for i, c in enumerate(citations):
        print(i+1)
        print(c)


        for i2 in range(c):
            print(i2)
        print("-------------------------------")


    return 0;



    # for h in range(N,0,-1):
    #     print(h)
    #     # if citations[h] >= h:
    #     #     return h
    # return 0



testData=  [4, 4, 4, 4, 3, 3, 3, 3, 5, 6, 6, 6, 6, 6,6]

print(solution(testData))# return 3