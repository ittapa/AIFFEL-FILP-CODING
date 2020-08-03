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


#testData
p1 = ["leo", "kiki", "eden"]
c1 = ["eden", "kiki"]

p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
c2  = ["josipa", "filipa", "marina", "nikola"]


p3= ["mislav", "stanko", "mislav", "ana"]
c3 = ["stanko", "ana", "mislav"]


'''

참가자랑 완주 list 를 정렬하고
비교한다. 비완주자는 한 명이기에
정렬한 두 리스트 값을 차례대로 비교, 다른 값이 범인 리턴 
비완주자가 마지막에 잇는 경우 를 위해
반복문안에서 해결안될을 시 마지막 참가자 리턴

'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]: return participant[i]
    return participant[-1]

r = solution(p2, c2) # vinko

print(r)

##다른 풀이
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
