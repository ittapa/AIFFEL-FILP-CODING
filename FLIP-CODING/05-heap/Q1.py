
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)


import heapq



def solution(scoville, K):

    answer = 0

    #heap으로 초기화
    heapq.heapify(scoville) # 알아서 정렬됨.
    print(scoville)
    print(len(scoville))


    while True:

        #전부 K가 넘었는지. 확인
        print(scoville[0])
        if scoville[0] >= K:
            return answer

        answer +=1 # 섞은 횟수 up

        # a1 = heapq.heappop(scoville) # 가장 낮은 음식
        # a2 = heapq.heappop(scoville)# 두번째로 낮은 음식)
        # d1 = a1 + a2*2 # 음식섞기
        # heapq.heappush(d1) # 다시 넣우지기.

        try: # run time error....
            heapq.heappush(scoville,  heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)) # 업데이드 된 음식 추가
        except:
            return -1


    return -1


i1 = [1, 2, 3, 9, 10, 12]
k1 = 7


r1 = solution(i1, k1)

print(r1)

