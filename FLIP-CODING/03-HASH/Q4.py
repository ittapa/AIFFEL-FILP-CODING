'''
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
'''

t1_g = ["classic", "pop", "classic", "classic", "pop"]
t1_p = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    cs = {} #카테고리 별 합계를 담는 딕
    cl = {} #카테고리 별 번호와 재생 수를 리스트로 담는
    for idx, c in enumerate(plays):
        # 장르 별 합 연산
        if genres[idx] in cs.keys():
            cs[genres[idx]] += c
        else:
            cs[genres[idx]] = c

        # 장르 별 List 분류
        if genres[idx] in cl.keys():
            cl[genres[idx]].append([idx, c])
        else:
            cl[genres[idx]] = [[idx, c]]

    #print(cl)

    # 장르별 합산 값 정렬
    cs = sorted(cs.items(), key=lambda item: item[1], reverse=True)  # value: [1]

    # 장르별  정렬 후 list 2개만 색출

    for c in cs:
        tl = sorted(cl[c[0]], key=lambda item: item[1], reverse=True) # 장르별 리스트 내용들 정렬.
        answer.append(tl[0][0])
        if len(tl) >= 2: answer.append(tl[1][0]) # 장르별 리스트가 1개일때 걸르기
    return answer

r1 = solution(t1_g, t1_p)
print(r1)
