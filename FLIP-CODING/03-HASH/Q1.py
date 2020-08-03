'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

https://programmers.co.kr/learn/courses/30/lessons/42576
'''


'''

결과 담을 dict 선언를(result,dict)

p(list)에 값을 c(list) 대조하여서 찾고
있는지 없는지 여부를 0,1 
p값과 여부 값을 결과
결과 담는 dict의 insert

+++++ 동명이인 처리


'''


#testData
p1 = ["leo", "kiki", "eden"]
c1 = ["eden", "kiki"]

p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
c2  = ["josipa", "filipa", "marina", "nikola"]


p3= ["mislav", "stanko", "mislav", "ana"]
c3 = ["stanko", "ana", "mislav"]



def solution(participant, completion):
    resultList = []  # 결론 정의할 dict 변수 선언
    listIndex = 0
    for p in participant:
        for c in completion:
            if p == c:
                completion.remove(c) # 제거 중복성
                print(completion)
                r =1 # 완주
            else :
                r=0 # 완주실패
                print("result", p)
                return p

                #return p
        resultList.insert(listIndex, {p:r})
        listIndex +=1

    print(resultList)
    return 0



#solution(p1, c1) # leo
r = solution(p2, c2) # vinko
print(r)








#동명이인 고려아함. ㅠ
def solution1(participant, completion):

    resultDict = {} #결론 정의할 dict 변수 선언.

    for p in participant:
        if p in completion :
            r = 1
        else:
            r = 0
        resultDict.update({p:r})

    for k in resultDict.keys():
        if resultDict.get(k) == 0: return k

    return 0



