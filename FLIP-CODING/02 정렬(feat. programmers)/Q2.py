'''
   문제정의
   정수를 받고,
   받은 정수를 배치하여 숫자들을 만들어보고,
   가장 큰 수를 골라서 문자열로 리턴.

'''



def solution(numbers):

    for num in numbers:
        print(num)

    answer = ''

    print(answer)
    return answer

testData = [6, 10, 2]
#[6102, 6210, 1062, 1026, 2610, 2106]
solution(testData)



'''
    1. 들어온 숫자 모든 형태로 조합 후 max => str 형변환
       - 모든형태 조합
'''