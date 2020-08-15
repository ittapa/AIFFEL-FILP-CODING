

def solution(priorities, location):
    answer = 0 # 현재 출력 순서 정보
    pl = [] # 순서대로 담긴 출력 우선수위와, 출력 여부 담기
    for p in priorities:
        pl.append([p, 0]) #기본 출력 여부는 0 출력하면 1

    while True :
        for index, p in enumerate(pl):
            if p[1] != 1:  # out 여부 체크
                if p[0] >= max([a[0] for a in pl if a[1]==0]): # 출력 안 한 것중에, 우선순위 최댓값 과 같거나 높은지 비교
                    p[1] = 1  # 출력 여부
                    answer +=1 # 출력순서 업
                    if index == location: # 출력한 index와 찾고자 하는 위치 index 같으면끝.
                        return answer



t1_p = [2, 1, 3, 2]
t1_l = 2
# r1  1

t2_p = [1, 1, 9, 1, 1, 1]
t2_l = 0
#r2 5

r1 = solution(t1_p, t1_l)
print(r1)


