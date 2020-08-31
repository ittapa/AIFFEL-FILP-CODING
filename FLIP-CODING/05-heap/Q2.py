
# 하나의 작업만 시행
# 각 걸린 시간의 평균.

import heapq


def solution(jobs):

    time = 0
    heapq.heapify(jobs) # heap으로

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
        ctimes.append(time - a1[1]) #요청시간으로 부터 걸린 시간 (현재시간 - 요청시간)

        for h in h2:
            v = heapq.heappop(h2)
            temp.append((v[1], v[0]))  # 다시 넣을 때 다시 시간기준으로 변경. task temp에.

        jobs = temp.copy()
        heapq.heapify(jobs)


    # 평균 출력
    return sum(ctimes) / len(ctimes)




def solution2(jobs):

    time = 0 # 현재시간,
    answer  = [] # job별 총 소요시간 입력 받는 변수.
    temp = []
    heapq.heapify(temp)

    while jobs:

        for j in jobs:
            if j[0] <= time:  # 현재시간보다 같거나 작은 task 는 시작가능.
                # 소요시간, 요청시간 소요시간순 정렬을 위해,
                heapq.heappush(temp, (j[1], j))


        if temp :
            #a = temp.pop(temp.index(heapq.nsmallest(1, temp)[0])) # 소요시간이 가장 큰 값.
            a = heapq.heappop(temp)
            time += a[0] # 현재시간 + 소요시간, 현재시간

            answer .append(time - a[1][0]) # 현 완료시간 - 요청시간 /  job 당 총 소요시간 요청시간~완료시간

            jobs.remove(a[1])
            temp =[]
        else :
            time +=1 # 현재 실행가능한 job이 없을 때,


    # 평균 출력
    return sum(answer) // len(answer)







# solution 실패
jobs1 = [[0, 3], [1, 9], [2, 6]]

# r1 = solution(jobs1)
# print(r1)

#solution 2

r2 = solution2(jobs1)
print(r2)