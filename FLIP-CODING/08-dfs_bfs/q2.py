'''

dfs& bfs
네트웤 ㅡ문제
https://programmers.co.kr/learn/courses/30/lessons/43162

'''

def solution1(n, computers):
    # 네트워크를 만들고 각각의 네트워크 갯수를 리턴.
    # 각 노드별 연결된 노드 체크 후
    # 연결된 노드가 없으면 네트워크 추가
    # 추가 되 있던 네트워크에 해당 노드가 있으면 그 노드에 추가하고 추가 연결된 노드는 합집합으로 추가.
    # 만약 여러개 네트워크에 연결되 잇으면 해당 네트워크들 다 합집합.

    # 연결된 노드끼리 묶어서 리스트 객체로 추가
    Networks = []

    # 노드별 연결된 노드 번호 색출
    for computer in computers: # 연결된 컴퓨터 정보 하나씩 색출.

        connected_computer_list = []
        for idx, connected in enumerate(computer):
            if connected :
                connected_computer_list.append(idx)

        # 기존 네트워크와 연결된 노드 비교 체크 (교집합)
        #  있으면 합집합해서 추가 아니면 새로 추가.
        # 여러개 노드에 연결되 있으면 .....
        # 연결된 네트워크 리스트에 일단 넣어 두었다가 마지막에 다 합침.
        temp_Networks = Networks[:]
        Networks = []
        connected_net_list =[connected_computer_list]

        while temp_Networks:
            net = temp_Networks.pop()
            if set(net) & set(connected_computer_list): # 교집합 체크.
                #net = list(set(net) | set(connected_computer_list)) # 합집합
                connected_net_list.append(net) # 연결된 네트워 리스트 변수에 일단 집어 넣기.

            else: # 연결되지 않는 네트워크는 바로 다시 추가.
                Networks.append(net)

        # 연결된 네트워크 리스트 합쳐서 네트워크리스트에 추가, 연결된게 없다면 자기자신 새로 추가. # reduce
        new_net = []
        while connected_net_list:
            new_net = list(set(new_net) | set(connected_net_list.pop()))
        Networks.append(new_net)

    print(Networks)
    #네트워크 개수.
    return len(Networks)



def solution(n, computers):
    # 네트워크를 만들고 각각의 네트워크 갯수를 리턴.
    # 각 노드별 연결된 노드 체크 후
    # 연결된 노드가 없으면 네트워크 추가
    # 추가 되 있던 네트워크에 해당 노드가 있으면 그 노드에 추가하고 추가 연결된 노드는 합집합으로 추가.
    # 만약 여러개 네트워크에 연결되 잇으면 해당 네트워크들 다 합집합.

    # 연결된 노드끼리 묶어서 리스트 객체로 추가
    Networks = []

    # 노드별 연결된 노드 번호 색출
    for computer in computers: # 연결된 컴퓨터 정보 하나씩 색출.

        connected_computer_list = []
        for idx, connected in enumerate(computer):
            if connected :
                connected_computer_list.append(idx)

        # 기존 네트워크와 연결된 노드 비교 체크 (교집합)
        #  있으면 합집합해서 추가 아니면 새로 추가.
        # 여러개 노드에 연결되 있으면 .....
        # 연결된 네트워크 리스트에 일단 넣어 두었다가 마지막에 다 합침.
        temp_Networks = Networks[:]
        Networks = []

        while temp_Networks:
            net = temp_Networks.pop()
            if set(net) & set(connected_computer_list): # 교집합 체크.
                #net = list(set(net) | set(connected_computer_list)) # 합집합
                #connected_net_list.append(net) # 연결된 네트워 리스트 변수에 일단 집어 넣기.
                connected_computer_list = list(set(connected_computer_list) | set(net))
            else: # 연결되지 않는 네트워크는 바로 다시 추가.
                Networks.append(net)

        Networks.append(connected_computer_list)

    print(Networks)
    #네트워크 개수.
    return len(Networks)

n1 = 3
c1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

r1 = solution(n1, c1)
print(r1)





'''
solution 1 
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.15ms, 10.1MB)
테스트 4 〉	통과 (0.14ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.53ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.1MB)
테스트 8 〉	통과 (0.45ms, 10.3MB)
테스트 9 〉	통과 (0.30ms, 10.1MB)
테스트 10 〉	통과 (0.30ms, 10.2MB)
테스트 11 〉	통과 (1.51ms, 10.3MB)
테스트 12 〉	통과 (1.27ms, 10.2MB)
테스트 13 〉	통과 (0.82ms, 10.3MB)



'''

'''
solution 
코드 일부 개선.

테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.1MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.44ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.41ms, 10MB)
테스트 9 〉	통과 (0.25ms, 10.2MB)
테스트 10 〉	통과 (0.24ms, 10.4MB)
테스트 11 〉	통과 (1.28ms, 10.3MB)
테스트 12 〉	통과 (1.12ms, 10.4MB)
테스트 13 〉	통과 (0.53ms, 10.2MB)

'''