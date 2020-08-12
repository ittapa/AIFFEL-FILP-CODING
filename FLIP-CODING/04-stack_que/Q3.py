## 최소시간

def solution(bridge_length, weight, truck_weights):

    answer = 0 #초로 취급
    #time = 0 # 초 시
    TL=[]  # 트럭 관련 정보를 담는 리스트
    current_w = 0  # 현재 다리위 트럭의 무게

    for t in truck_weights:
        TL.append([t,bridge_length+1,0]) # 0 트럭의 무게 / 1 남은 거리 / 2 현재상태(0:대기, 1:건너가는중)

    while(True):
        # 1초 가 간다 ....틱톡
        answer += 1

        #다리위에 최대한 트럭 올리기
        #올라온 트럭들 한걸음씩 가기
        for t in TL:
            if t[1] > 0:# 다리를 다 안 건넜으면.
                if t[2] == 1: # 이미 건너가는 중이면
                    t[1] -= 1  # 한걸음가기
                else: # 건너가는 중이 아니면
                    if current_w + t[0] <= weight: # 트럭을 추가했을때 초과하는지 체크하고
                        t[2] = 1 # 상태 건너가는중으로 변경.
                        current_w += t[0] # 현재 다리위 트럭 무게에 추가
                        t[1] -= 1  # 한걸음가기면
                        #break; # 트럭이 1초에 1대 씩 올라갈수 있음.

        ct = 0; #다 건넌 트럭 수 .
        for t in TL:
            if t[1] == 0 : # 다 건 넜으면..
                t[1] = -1
                current_w -= t[0] # 현재 다리위 무게 제거.
            if t[1] == -1:
                ct+=1

        # 다 건넌는지를 체크
        if ct == len(TL):
            return answer


t1_bl = 2
t1_w = 10
t1_tw = [7,4,5,6]

r1 = solution(t1_bl,t1_w,t1_tw)
print(r1)

