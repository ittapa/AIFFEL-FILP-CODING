'''

여행경로

https://programmers.co.kr/learn/courses/30/lessons/43164


항상 ICN 출발
'''

def solution(tickets):

    # 시작은 인천
    # 경로2개일대는 알파벳 순.

    # 가지고 있는 Tickets 들중 현재 위치에서 다음 티켓을 찾는 함수 정의
    # @return 갈수 있는 티켓들 반환
    def find_next_tickets(current_position):
        temp_t = []
        for t in tickets:
            if t[0] == current_position:
                temp_t.append(t)
        #정렬
        temp_t.sort()

        return temp_t



    #함수정의 : 출발지 정보로, 티켓을 찾고, 여러개 일때는 알파뱃 순 정렬.해서 첫번째 값 리턴.
    def findByD(depature):

        next_tickets = find_next_tickets(depature)

        # 티켓이 남아 있는데, 알파뱃으로 정렬한 우선순위 티켓이 다음 목적지가 없는 경우 체크 후
        # 차순위 티켓으로 변경
        next_ticket = []
        if len(next_tickets) == 1:
            next_ticket = next_tickets[0]
        else:
            for c_t in next_tickets:
                checked = find_next_tickets(c_t[1])
                if checked:
                    next_ticket = c_t
                    break

        #print(next_ticket)
        answer.append(next_ticket[1])
        tickets.remove(tickets[tickets.index(next_ticket)]) # 티켓리스트에서 제거.

        if tickets :
            findByD(next_ticket[1])

    answer = ["ICN"]
    findByD("ICN")

    return answer



# t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# r1 = solution(t1)
# print(r1)

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