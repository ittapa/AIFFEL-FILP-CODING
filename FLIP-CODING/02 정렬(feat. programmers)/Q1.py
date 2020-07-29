
def solution(array, commands):
    answer = []
    for com in commands:
        alist = array[com[0] - 1:com[1]]
        alist.sort()
        answer.append(alist[com[2] - 1])
        #print(array[com[0] - 1:com[1]].sort()[com[2] - 1]) .......
    print(answer)
    return answer

# test Data
array, commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)
