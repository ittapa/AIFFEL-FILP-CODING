'''
	문제 정의
    1. data import
      - 케이스 수  T
      - 이동정류장수(k), 종점정류장(n), 충전 정류장 수 정의(m)
      - 충전정류장 list (mList)
    2. return
      - 종점 최소경로 도달 후 충전횟 수 출, 종점 도달 실패 시 0 출력
    3. 조건
      - 최초 풀 충전, 충천횟수 미포함
    4. 케이스별 순환 연산
'''

T = int(input())

for test_case in range(1, T + 1):

    #data import
	k,n,w = map(int, input().split(" "))
	mList =  list(map(int, input().split(" ")))
	mList.sort();  # 오름차순 정렬

	efList = []  # 최적 충전 정류장을 담는 변
	hp = k  # 현재 충전상태

	# 정류장 하나씩 이동.
	for cp in range(1, n):

		hp -= 1  # 충전거리 감소

		# 배터리 고갈
		if k < 0:
			result = 0
			break

		# 최적의 경로 찾기
		if cp in mList:
			nextP = mList[mList.index(cp):][1] # 다음정류장 조회
			if nextP - cp > hp & nextP > cp+k :  # 다음정류장 갈 수 있는지 체크 후 충전 및 데이터입력
				hp = k  # 충전
				efList.append(cp)
				# 목적지 도착 전 마지막 충전.
				if cp + hp >= n:
					result = len(efList)
					break

			if cp+hp < nextP: #다음 정류장까지 못가는 경우
				result = 0
				break

	print("#{} {}".format(test_case, result))