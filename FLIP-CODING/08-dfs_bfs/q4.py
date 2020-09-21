'''

여행경로

https://programmers.co.kr/learn/courses/30/lessons/43164


항상 ICN 출발
'''

def solution(tickets):

    # 시작은 인천
    # 경로2개일대는 알파벳 순.


    #함수정의 : 출발지 정보로, 티켓을 찾고, 여러개 일때는 알파뱃 순 정렬.해서 첫번째 값 리턴.
    def find_by_depature(depature, temp_tickets, temp_answer):

        next_tickets = []
        for t in temp_tickets:
            if t[0] == depature:
                next_tickets.append(t)
        # 정렬
        next_tickets.sort()

        if len(next_tickets) == 0: 
            return 0
        
        #다음 티켓들 꺼내서 dfs 수행
        for ticket in next_tickets:
            temp_answer_copy = temp_answer[:]
            temp_answer_copy.append(ticket[1])

            temp_tickets_copy = temp_tickets[:]
            temp_tickets_copy.remove(temp_tickets_copy[temp_tickets_copy.index(ticket)]) # 티켓리스트에서 제거.
            print(temp_answer_copy)

            if temp_tickets_copy :
                result = find_by_depature(ticket[1], temp_tickets_copy, temp_answer_copy)

                if result == 0:
                    temp_tickets.append(ticket) # 다시 넣어주기
                    continue
                else :
                    return result
            else:
                return temp_answer_copy


    return find_by_depature("ICN", tickets, ["ICN"])


t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
r1 = solution(t1)
print(r1)

print("--------------")

t2 = [["ICN", "JFK"], ["ICN", "ABC"], ["JFK", "HND"],["HND", "ICN"]]
r2 = solution(t2)
print(r2)



## 알파벳 순으로 했을때 도달하지 못하는경우.


'''
첫번째 코드
테스트 1 〉	실패 (런타임 에러)
테스트 2 〉	실패 (런타임 에러)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
'''


'''

   # 티켓이 남아 있는데, 알파뱃으로 정렬한 우선순위 티켓이 다음 목적지가 없는 경우 체크 후
        # 차순위 티켓으로 변경
테스트 1 〉	실패 (런타임 에러)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)

'''