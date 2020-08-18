## 최소시간

def solution(bridge_length, weight, truck_weights):
    answer = 0  # 초로 취급
    TL = []  # 트럭 관련 정보를 담는 리스트
    current_w = 0  # 현재 다리위 트럭의 무게
    ct = 0  # 완료된 트럭수
    tt = len(truck_weights)  # 총 트럭 수.

    for t in truck_weights:
        TL.append([t, bridge_length])  # 0 트럭의 무게 / 1 남은 거리 / 2 현재상태(0:대기, 1:건너가는중)

    print(answer, current_w, TL, ct, tt)
    while True:
        # 1초 가 간다 ....틱톡
        answer += 1
        for t in TL:
            if t[1] == 0:  # 다리 다건넜으면 [1] = 0
                t[1] = -1  # -1 다겄넘..
                current_w -= t[0]  # 현재 다리 무게 제거
                ct += 1
                # 다 건넜는지를 체크
                if tt == ct:
                    print(answer, current_w, TL, ct, tt)
                    return answer
                break # 1차선 도로라 하나임.

        # 다리위에 최대한 트럭 올리기
        # 올라온 트럭들 한걸음씩 가기
        # 순서대로
        for t in TL:

            if t[1] != -1:  # 다리를 다 안 건넜으면.

                if t[1] == 2:  # 건너가는 중이 아니면
                    if current_w + t[0] <= weight:  # 트럭을 추가했을때 제한 초과하는지 체크
                        current_w += t[0]  # 현재 다리위 트럭 무게에 추가
                        t[1] -= 1  # 한걸음가기
                    break  # 일차산 다리라 트럭이 1대 씩 올라갈수 있음.


                else:  # 이미 건너가는 중이면
                    t[1] -= 1  # 한걸음가기
        print(answer, current_w, TL, ct, tt)





t1_bl = 2
t1_w = 10
t1_tw = [7, 4, 5, 6] # 7456

r1 = solution(t1_bl, t1_w, t1_tw)
print(r1)
