'''
타겟넘버
https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

'''

def solution(numbers, target):

    temp_list = []

    while numbers:
        num = numbers.pop()

        #최초.
        if len(temp_list) == 0:
            temp_list.append(+num)
            temp_list.append(-num)
        else:
            temp_list2 = temp_list[:]
            temp_list =[]
            while temp_list2:
                temp_nums = temp_list2.pop()
                temp_list.append(temp_nums+num) # + 연산
                temp_list.append(temp_nums-num) # - 연산

    return temp_list.count(target) #


n1=[1, 1, 1, 1, 1]
t1 = 3

r1 = solution(n1, t1)
print(r1)

'''
테스트 1 〉	통과 (201.69ms, 41.9MB)
테스트 2 〉	통과 (200.79ms, 39.8MB)
테스트 3 〉	통과 (0.32ms, 10.2MB)
테스트 4 〉	통과 (1.15ms, 10.2MB)
테스트 5 〉	통과 (6.61ms, 10.8MB)
테스트 6 〉	통과 (0.35ms, 10.3MB)
테스트 7 〉	통과 (0.31ms, 10.2MB)
테스트 8 〉	통과 (2.04ms, 10.4MB)
'''

