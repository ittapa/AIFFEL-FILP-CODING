'''

	문제 정의
    1. 케이스 숫자 input  T
    2. 케이스별 순환 연산
      2-1. 케이스 별 이동 최대 이동정류장수(k), 종점정류장(n), 충전 정류장 수 정의(m)      
      2-2. 케이스 별 충전 정류장 번호 정의 mList
      2-3. 최소 종점 도달 충전횟수 도출  
              ****** 종점 --1 충전정류장 찾기
              최대이동정류장수 초과시 실패 0출력
      2-4 결과 출력, 도달 실패시 0< 출력
'''
T = int(input())
print(T)

for test_case in range(1, T + 1):
	k,n,w = map(int, input().split(" "))
	#print(k,n,w)
    
    #최악의 수 미리 배제, 이미 종점갈 충전정류장이 모자란 경우, 
    if(n > 3+(k*m):
        print(0)
        continue

	mList =  list(map(int, input().split(" ")))
	mList.sort(); # 오름차순 정렬
	#print(mList)
    
    # 2-1. 케이스 별 이동 최대 이동정류장수(k), 종점정류장(n), 충전 정류장 수 정의(m)      
	moveCount = 0
	for a in range(0, n):
		moveCount +=moveCount
		
        #충전소 찾기 충전소 있으면 충전후 이동거리 초기화
        
        
    	#충전소 가 최대 이동거리내에 없을 때 
		if(moveCount > k):
			print(0)
			continue
