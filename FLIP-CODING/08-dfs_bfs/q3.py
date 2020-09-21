'''

단어변환

https://programmers.co.kr/learn/courses/30/lessons/43163

'''



def solution(begin, target, words):
    answer = 0
    # 각 단어별 target 단어가 있는 문자 번호들 색출

    t_list =[]

    for n_idx, t in enumerate(target):
        temp = []
        for w_idx, w in enumerate(words):
            if t == w[n_idx]:
                temp.append(w_idx)

        # 하나도 없을때,
        #if temp : return 0
        t_list.append(temp)

    print(t_list) #

    return answer

b1 = "hit"
t1 = "cog"
w1 = ["hot", "dot", "dog", "lot", "log", "cog"]

r1 = solution(b1, t1, w1)
