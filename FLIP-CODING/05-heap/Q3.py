
import heapq


def solution(operations):

    temp =[]
    #heapq.heapify(temp)

    for o in operations:
        key, value = o.split() # 문자 분해
        #print(key, value) # 알파뱃, 숫자

        if key == 'I':
            temp.append(int(value))# 숫 자 형변환

        elif len(temp) > 0 : # temp가  # key == 'D'
            print("m: ", heapq.nlargest(1, temp)[0])  #nlargest n개의 큰수 리스트로 반환.
            print("s: ", heapq.nsmallest(1, temp)[0])
            if value == '1': # 최대값 삭제
                temp.pop(temp.index(heapq.nlargest(1, temp)[0]))
            else: # value =='-1' 최소값 삭제
                temp.pop(temp.index(heapq.nsmallest(1, temp)[0]))

    if len(temp) == 0: temp.append(0) # 없을 때,, 방지
    print(temp)

    return [max(temp), min(temp)]



#
# o1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# #o1 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# r1 = solution((o1))
#
# print(r1) # [0,0]

o2 = ["I 7","I 5","I -5","D -1"]
r2 = solution((o2))

print(r2) # [7,5]