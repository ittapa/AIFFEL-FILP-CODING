# 1. 케이스 개수 도출 = T
 # 2. 케이스별 순환문 작성
    #2-1 케이스의 정수 개수 도출
    #2-2 케이스별 입력값 도출후 형변환
    #2-3 케이스별 최댓값, 최솟값 도출
    #2-4 케이스 최댓값 최솟값 차이 연산후 출력

T = int(input()) # 케이스 개수
    
#print(T)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    ea = int(input()) # 케이스 정수 개수
    #print(test_case ,"번째 케이스의 정수 개수는 ",ea) 
    
    nums =  list(map(int, input().split(" "))) # 케이스별 입력값 도출 후 형변환
    
    minNum = min(nums)
    maxNum = max(nums)
    #print(test_case ,"번째 케이스의 min ",minNum) 
    #print(test_case ,"번째 케이스의 max ",maxNum)
    
    result = maxNum - minNum
    #print(test_case ,"번째 케이스의 result ",result) 
    #print("#", test_case, result) 
    print("#{} {}".format( test_case, result))

