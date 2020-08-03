'''
   문제정의
   정수를 받고,
   받은 정수를 배치하여 숫자들을 만들어보고,
   가장 큰 수를 골라서 문자열로 리턴.

    numbers의 길이는 1 이상 100,000 이하입니다.
    numbers의 원소는 0 이상 1,000 이하입니다.
    정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

문자열 비교연산
문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다
1000이면 가장 뒤에오는게 베스트
999 가장 앞
034 3자리로 만들고 하나씩 비교해서
앞자리가 큰순서대로 정렬

문자열 곱하기 연산


'''
#


def solution(numbers):

    strNums = sorted(list(map(str, numbers)),key=lambda x: x * 3, reverse=True)
    # 문자열 리스트로 받고
    # 3자라 이상으로 만들어서 정렬, 내림차순,
    # 문자열 sort  index 0 ~ 부터 비교
    #print(strNums)

    answer = ''
    for s in strNums:
        answer += s

    # 맨 앞이 0인 경우
    if answer[0] == '0':
        answer = str(int(answer))


    print(answer)
    return answer

testData = [6, 10, 2]


#[6102, 6210, 1062, 1026, 2610, 2106]
solution(testData)



'''
    1. 들어온 숫자 모든 형태로 조합 후 max => str 형변환
       - 모든형태 조합
'''