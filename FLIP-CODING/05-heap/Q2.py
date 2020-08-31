
# 하나의 작업만 시행
# 각 걸린 시간의 평균.

import heapq


def solution(jobs):

    time = 0
    heapq.heapify(jobs) # heap으로 초기화
    ctimes = []


    ## 정렬기준1, 요청시간, 정렬기준2 -걸리는시간
    while jobs :

        h2 = [] # 현재시간에서 실행가능한 task를 걸리는 시간기준으로 재정렬한 힙.
        temp = []

        # 현재 시간에 서 대기중인 task중 걸리는 시간 기준 재정렬 후 선별.
        while jobs:
            a = heapq.heappop(jobs)
            if a[0] <= time: # 현재시간보다 같거나 작은 task 는 시작가능.
                # h2 힙에 할당.
                #heapq.heappush(h2, (a[1] , a[0])) # 걸리는 시간 기준 재정렬 ,,
                h2.append((a[1] , a[0]))
            else:
                temp.append(a)# 다시 넣을 task temp에.

        #jobs 실행 불가능 task 다시 넣기.

        # 현재시간에서 가능한 테스크 (걸리는시간 이
        heapq.heapify(h2)
        a1 = heapq.heappop(h2) # 가장 요청이 가장 빠른 우선순위
        time += a1[0]  # 처리시간 ++ ( 현재시간 + 걸린시간)
        ctimes.append(time -a1[1]) #요청시간으로 부터 걸린 시간 (현재시간 - 요청시간)

        for h in h2:
            v = heapq.heappop(h2)
            temp.append((v[1], v[0]))  # 다시 넣을 때 다시 시간기준으로 변경. task temp에.

        jobs = temp.copy()
        heapq.heapify(jobs)


    # 평균 출력
    answer = sum(ctimes) / len(ctimes)


    return answer







jobs1 = [[0, 3], [1, 9], [2, 6]]

r1 = solution(jobs1)

print(r1)