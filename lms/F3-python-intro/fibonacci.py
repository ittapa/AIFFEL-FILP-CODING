'''
    피보나치킨(?)
    n명의 사람은 피보나치 수열 n-1번째 만큼의
    치킨을 흡입한다.
    - 피보나치수열 함수 define

'''

#피보나치 함수 정
def fibonacci(n):
    if n <=2 :
        number = 1
    else :
        number = fibonacci(n-1) + fibonacci(n-2)
    return number

print(fibonacci(10))

#효율성 증대
memory = {1:1, 2:1}
def fibonacci2(n):
    if n in memory:
        number = memory[n]
    else :
        number = fibonacci2(n-1) + fibonacci2(n-2)
        memory[n] = number
    return number
print(fibonacci2(100))


print(memory)