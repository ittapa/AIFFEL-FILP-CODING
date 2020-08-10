'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.

'''

'''
전화번호 하나씩 꺼내기 for 문.
다른 전화에 접두어인지 비교하기
 - 아니면 계속 
 - 맞으면 return answer=false
 - 끝가지 아니면 true
'''

t1 = ["119", "97674223", "1195524421"]
t2 = ["123","456","789"]
t3 = ["12","123","1235","567","88"]

def solution(phone_book):
    l = len(phone_book)
    phone_book = list(map(str, sorted(list(map(int, phone_book),))))
    for i, strNum in enumerate(phone_book):
        for i2 in range(i+1, l):
            if phone_book[i2].startswith(strNum):
                return False
    return True

print(solution(t1))
print(solution(t2))
print(solution(t3))










#
#
# phone_book_d = { p: value for p in phone_book}
#
# [p[:i + 1] for i in range(len(p))]
#
# for p in phone_book:
#     defd
#
