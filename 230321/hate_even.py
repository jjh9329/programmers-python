def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2 !=0 :
            answer.append(i)
    
    return answer

# 다른사람이 푼 식
def solution(n):
    return [i for i in range(1, n+1, 2)]

print(solution(15))