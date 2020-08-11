t1_p =[93,30,55]
t1_s =[1,30,5]

def solution(progresses, speeds):

    answer = [] # 정답
   # day = 0 #1
    L1 = [] # 현재 진행도와 하루 진행량 , 완 여부, 배포 여부
    ac = False  # 완료 여부

    #L1 초기화
    for idx in range(len(progresses)):
        L1.append([progresses[idx], speeds[idx], 0 , 0])


    while(not ac):
        #day = day +1 # 또 하루가 간다.

        for idx in range(len(L1)):
            if L1[idx][2] != 1:
                L1[idx][0] = L1[idx][0] +L1[idx][1]  # 현재 진행도= 현재 진행도 + 하루 진행량.
                if(L1[idx][0] >= 100): # 현재 진행도 100% 돌파시 .......
                    L1[idx][2] =1 # 완료
            else:
                pass
                #완료, 제거하기

        count = 0 #배포 수를 담는 변수. 초기
        for idx in range(len(L1)):
            if L1[idx][2] == 1 : # 완료했고
                if L1[idx][3] ==0 : # 배포 안했으면
                    L1[idx][3] = 1 # 배포 상태로 변경.
                    count = count+1
            else: # 순서대로 하나라도 안걸리면 for문 아웃 배포안함.
                break;

        # count 0 이 아니라면
        if count != 0:
            answer.append(count)

        # 전부 배포 여부 체크
        if 0 in (l[2] for l in L1):
            pass
        else:
            ac = True
    return answer

r1= solution(t1_p, t1_s)
print("r1", r1)
