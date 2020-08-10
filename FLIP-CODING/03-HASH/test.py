#### hash
#### deictionary
####


def solution(genres, plays):
    answer = []
    genres_play = {}

    # 장르별 플레이 수 구하기
    for genre, play in zip(genres, plays):
        if genre in genres_play.keys():
            genres_play[genre] += play
        else:
            genres_play[genre] = play

    # 플레이 수를 기준으로 장르 순위 결정
    genre_rank = [genre for genre, play in sorted(genres_play.items(), key=lambda x: x[1], reverse=True)]

    # 고유번호 dictionary로 저장
    # key = (장르, 고유번호) value = 플레이 수
    id_ = {(g_p[0], i): g_p[1] for i, g_p in enumerate(zip(genres, plays))}

    # 플레이 수를 기준으로 노래들 정렬하여, 장르와 고유번호 list로 저장
    song_rank = [g_i for g_i, play in sorted(id_.items(), key=lambda x: x[1], reverse=True)]

    for gr in genre_rank:
        count = 0
        for song in song_rank:
            if count == 2:
                break
            # 노래가 해당 장르이면, 고유번호 추가
            if gr in song:
                answer.append(song[1])
                count += 1

    return answer

t1_g = ["classic", "pop", "classic", "classic", "pop"]
t1_p = [500, 600, 150, 800, 2500]

from collections import defaultdict
import heapq
import operator
def solution2(genres, plays):
    play_genre = defaultdict(int)
    best_play = defaultdict(list)

    for idx, val in enumerate(genres):
        p = plays[idx]
        play_genre[val] += p
        heapq.heappush(best_play[val], [-p, idx])

    answer = []
    for item in sorted(play_genre.items(), key = operator.itemgetter(1), reverse = True):
        genre = item[0]
        answer += [heapq.heappop(best_play[genre])[1]]
        if best_play[genre]:
            answer += [heapq.heappop(best_play[genre])[1]]

    return answer

r1 = solution2(t1_g, t1_p)
print(r1)